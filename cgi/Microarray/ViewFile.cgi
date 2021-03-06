#!/usr/local/bin/perl

###############################################################################
# Set up all needed modules and objects
###############################################################################
use strict;
use Getopt::Long;
use FindBin;

use lib qw (../lib/perl ../../lib/perl);

use vars qw ($sbeams $sbeamsMOD $q $dbh $current_contact_id $current_username
             $PROG_NAME $USAGE %OPTIONS $QUIET $VERBOSE $DEBUG $DATABASE
             $current_work_group_id $current_work_group_name
             $current_project_id $current_project_name
             $TABLE_NAME $PROGRAM_FILE_NAME $CATEGORY $DB_TABLE_NAME
             $PK_COLUMN_NAME @MENU_OPTIONS);
#use CGI;
use CGI::Carp qw(fatalsToBrowser croak);

use SBEAMS::Connection qw($q);
use SBEAMS::Connection::Settings;
use SBEAMS::Connection::Tables;
use SBEAMS::Connection::TableInfo;
#$q = new CGI;
$sbeams = new SBEAMS::Connection;

use SBEAMS::Microarray;
use SBEAMS::Microarray::Settings;
use SBEAMS::Microarray::Tables;
use SBEAMS::Microarray::TableInfo;
$sbeamsMOD = new SBEAMS::Microarray;

$sbeamsMOD->setSBEAMS($sbeams);
$sbeams->setSBEAMS_SUBDIR($SBEAMS_SUBDIR);


###############################################################################
# Set program name and usage banner for command like use
###############################################################################
$PROG_NAME = $FindBin::Script;
$USAGE = <<EOU;
Usage: $PROG_NAME 
Options:
  --verbose n         Set verbosity level.  default is 0
  --quiet             Set flag to print nothing at all except errors
  --debug n           Set debug flag

 e.g.:  $PROG_NAME [OPTIONS] [keyword=value],...

EOU

#### Process options
unless (GetOptions(\%OPTIONS,"verbose:s","quiet","debug:s")) {
  print "$USAGE";
  exit;
}

$VERBOSE = $OPTIONS{"verbose"} || 0;
$QUIET = $OPTIONS{"quiet"} || 0;
$DEBUG = $OPTIONS{"debug"} || 0;
if ($DEBUG) {
  print "Options settings:\n";
  print "  VERBOSE = $VERBOSE\n";
  print "  QUIET = $QUIET\n";
  print "  DEBUG = $DEBUG\n";
}



###############################################################################
# Set Global Variables and execute main()
###############################################################################

my $FILE_BASE_DIR = "/net/arrays/Pipeline/output/project_id";
my $DOC_BASE_DIR = "";
my $DATA_READER_ID = 40;

main();
exit(0);



###############################################################################
# Main Program:
#
# Call $sbeams->InterfaceEntry with pointer to the subroutine to execute if
# the authentication succeeds.
###############################################################################
sub main {

  #### Do the SBEAMS authentication and exit if a username is not returned
  exit unless ($current_username = $sbeams->Authenticate(
    #connect_read_only=>1,
    #allow_anonymous_access=>1,
    #permitted_work_groups_ref=>['Proteomics_user','Proteomics_admin'],
  ));

  #### Read in the default input parameters
  my %parameters;
  my $n_params_found = $sbeams->parse_input_parameters(
    q=>$q,parameters_ref=>\%parameters);
  #$sbeams->printDebuggingInfo($q);

  #### Define standard variables
  my $file_name = $parameters{'FILE_NAME'}
  || die "ERROR: file not passed";
  my $action =$parameters{'action'} || "download";
  my $project_id = $parameters{'project_id'} || $sbeams->getCurrent_project_id;


  ## Output Directory depends on what file type
  my $output_dir;
  if ($file_name =~ /\.map$/ || $file_name=~/\.key$/) {
	$output_dir = "/net/arrays/Slide_Templates";
  }elsif ($file_name =~/\.doc/){
	$output_dir = "/net/";
  }elsif ($file_name eq "matrix_output") {
	$output_dir = "$FILE_BASE_DIR/$project_id";
  }elsif ($file_name =~/\d+\_constants_file/) {
	$output_dir = "$PHYSICAL_BASE_DIR/data/MA_experiment_constants";
  }else {
	$output_dir = "$FILE_BASE_DIR/$project_id";
  }

  ## Get other helpful variables
  my $subdir = $parameters{SUBDIR};


  ## Process File Path
  my $file_path = "$output_dir/$subdir/$file_name";

  if ($action eq 'download') {
	if ($sbeams->get_best_permission <= $DATA_READER_ID){
	  print "Content-type: application/force-download \n";
	  print "Content-Disposition: filename=$file_name\n\n";
	  my $buffer;
	  open (DATA, "$file_path")
		|| die "Couldn't open $file_name";
	  while(read(DATA, $buffer, 1024)) {
		print $buffer;
	  }
	  close (DATA);
	}else {
	  $sbeams->printPageHeader();
	  print qq~
		<BR><BR><BR>
		<H1><FONT COLOR="red">You Do Not Have Access To View This File</FONT></H1>
		<H2><FONT COLOR="red">Contact PI or another administrator for permission</FONT></H2>
		~;
	  $sbeamsMOD->printPageFooter();
	}
  }

  elsif ($action eq 'view_image'){
	linkImage(file=>$file_path);
	$sbeamsMOD->printPageFooter();
  }

  elsif($action eq 'read' && $sbeams->get_best_permission <= $DATA_READER_ID){
	  print "Content-type: text/html\n\n";
	  print ($file_path);
	  if (!printFile(file=>$file_path)){
		print qq~
	  $file_path COULD NOT BE OPENED FOR VIEWING
      ~;
	  }
  }

  else {

	$sbeamsMOD->printPageHeader();	
	
	#### Verify user has permission to access the file
	my $success = 0;
	if ($sbeams->get_best_permission <= $DATA_READER_ID){
	  my $file = "$output_dir/$file_name";
	  $success = printFile(file=>$file);
	}
	if (!$success) {
	  print qq~
		<BR><BR><BR>
		<H1><FONT COLOR="red">You Do Not Have Access To View This File</FONT></H1>
		<H2><FONT COLOR="red">Contact PI or another administrator for permission</FONT></H2>
		~;
	}

	$sbeamsMOD->printPageFooter();
  }

} # end main




###############################################################################
# linkImage
#
###############################################################################
sub linkImage {
  my %args = @_;
  my $file = $args{'file'};
  my $error = 0;
  open(INFILE, "< $file") || sub{$error = -1;};

  if ($error == 0) {
			print "Content-type: image/jpeg\n\tname=\"file.jpg\"";
			print "Content-Transfer-Encoding: base64\n";
			print "Content-Disposition: inline\n";
			print "\n";

			my $buffer;
			open (IMAGE, "$file") || die "Couldn't open $file";
			binmode(IMAGE);
			while(read(IMAGE,$buffer,1024)){
				print $buffer;
			}
  }
  else{
      print qq~
	  $file
	  <CENTER><FONT COLOR="red"><h1><B>FILE COULD NOT BE OPENED FOR VIEWING</B></h1>
	  Please report this to <a href="mailto:mailto:mjohnson\@systemsbiology.org">Michael Johnson</a>
	  </FONT></CENTER>
      ~;
  }
	  
} # end linkImage

###############################################################################
# printFile
#
# A very simple script.  Throw the contents of the file within <PRE> tags and
# we're done
###############################################################################
sub printFile {
  my %args = @_;

  my $file = $args{'file'};
  my $error = 0;

  open(INFILE, "< $file") || sub{$error = -1;};

  if ($error == 0) {
	while (<INFILE>) {
	  print qq~ $_ ~;
	}
	return 1;
  }
  return 0;
} # end printFile


