package SBEAMS::Connection::Tables;

###############################################################################
# Program     : SBEAMS::Connection::Tables
# Author      : Eric Deutsch <edeutsch@systemsbiology.org>
# $Id$
#
# Description : This is part of the SBEAMS::Connection module which provides
#               a level of abstraction to the database tables.
#
# SBEAMS is Copyright (C) 2000-2005 Institute for Systems Biology
# This program is governed by the terms of the GNU General Public License (GPL)
# version 2 as published by the Free Software Foundation.  It is provided
# WITHOUT ANY WARRANTY.  See the full description of GPL terms in the
# LICENSE file distributed with this software.
#
###############################################################################

use strict;

use SBEAMS::Connection::Settings;


use vars qw(@ISA @EXPORT 
    $TB_USER_LOGIN
    $TB_WORK_GROUP
    $TB_USER_WORK_GROUP
    $TB_USER_CONTEXT
    $TB_RECORD_STATUS
    $TB_PRIVILEGE
    $TB_CONTACT_TYPE
    $TB_CONTACT
    $TB_ORGANIZATION_TYPE
    $TB_ORGANIZATION
    $TB_PROJECT
    $TB_USER_PROJECT_PERMISSION
    $TB_GROUP_PROJECT_PERMISSION
    $TB_DBXREF
    $TB_ORGANISM

    $TB_TABLE_COLUMN
    $TB_TABLE_PROPERTY
    $TB_TABLE_GROUP_SECURITY
    $TB_SQL_COMMAND_LOG
    $TB_USAGE_LOG
    $TB_HELP_TEXT
    $TB_MISC_OPTION
    $TB_QUERY_OPTION
    $TB_CACHED_RESULTSET
    $TB_FORM_TEMPLATE
    $TB_SHORT_URL

    $TB_MGED_ONTOLOGY_RELATIONSHIP
    $TB_MGED_ONTOLOGY_TERM
    $TB_ONTOLOGY_RELATIONSHIP_TYPE
    $TB_ONTOLOGY_TERM_TYPE

    $TB_SOFTWARE_HARDWARE_PROTOCOL
    $TB_PROTOCOL
    $TB_PROTOCOL_TYPE

    $TB_TEST_PROTOCOL
    $TB_TEST_SAMPLE
    $TB_TEST_SAMPLE_PROTOCOL

    $TB_PROJECT_FILE
);


require Exporter;
@ISA = qw (Exporter);

@EXPORT = qw (
    $TB_USER_LOGIN
    $TB_WORK_GROUP
    $TB_USER_WORK_GROUP
    $TB_USER_CONTEXT
    $TB_RECORD_STATUS
    $TB_PRIVILEGE
    $TB_CONTACT_TYPE
    $TB_CONTACT
    $TB_ORGANIZATION_TYPE
    $TB_ORGANIZATION
    $TB_PROJECT
    $TB_USER_PROJECT_PERMISSION
    $TB_GROUP_PROJECT_PERMISSION
    $TB_DBXREF
    $TB_ORGANISM

    $TB_TABLE_COLUMN
    $TB_TABLE_PROPERTY
    $TB_TABLE_GROUP_SECURITY
    $TB_SQL_COMMAND_LOG
    $TB_USAGE_LOG
    $TB_HELP_TEXT
    $TB_MISC_OPTION
    $TB_QUERY_OPTION
    $TB_CACHED_RESULTSET
    $TB_FORM_TEMPLATE
    $TB_SHORT_URL

    $TB_MGED_ONTOLOGY_RELATIONSHIP
    $TB_MGED_ONTOLOGY_TERM
    $TB_ONTOLOGY_RELATIONSHIP_TYPE
    $TB_ONTOLOGY_TERM_TYPE

    $TB_SOFTWARE_HARDWARE_PROTOCOL
    $TB_PROTOCOL
    $TB_PROTOCOL_TYPE

    $TB_TEST_PROTOCOL
    $TB_TEST_SAMPLE
    $TB_TEST_SAMPLE_PROTOCOL

    $TB_PROJECT_FILE
);



#### Get the appropriate database prefix for the SBEAMS core
my $core = $DBPREFIX{Core};


#### Define the physical table names
$TB_USER_LOGIN          = "${core}user_login";
$TB_WORK_GROUP          = "${core}work_group";
$TB_USER_WORK_GROUP     = "${core}user_work_group";
$TB_USER_CONTEXT        = "${core}user_context";
$TB_RECORD_STATUS       = "${core}record_status";
$TB_PRIVILEGE           = "${core}privilege";
$TB_CONTACT_TYPE        = "${core}contact_type";
$TB_CONTACT             = "${core}contact";
$TB_ORGANIZATION_TYPE   = "${core}organization_type";
$TB_ORGANIZATION        = "${core}organization";
$TB_PROJECT             = "${core}project";
$TB_USER_PROJECT_PERMISSION     = "${core}user_project_permission";
$TB_GROUP_PROJECT_PERMISSION    = "${core}group_project_permission";

$TB_DBXREF              = $DBPREFIX{BioLink}."dbxref";
$TB_ORGANISM            = "${core}organism";

$TB_TABLE_COLUMN        = "${core}table_column";
$TB_TABLE_PROPERTY      = "${core}table_property";
$TB_TABLE_GROUP_SECURITY= "${core}table_group_security";
$TB_SQL_COMMAND_LOG     = "${core}sql_command_log";
$TB_USAGE_LOG           = "${core}usage_log";
$TB_HELP_TEXT           = "${core}help_text";
$TB_MISC_OPTION         = "${core}misc_option";
$TB_QUERY_OPTION        = "${core}query_option";
$TB_CACHED_RESULTSET    = "${core}cached_resultset";
$TB_FORM_TEMPLATE       = "${core}form_template";
$TB_SOFTWARE_HARDWARE_PROTOCOL = "${core}software_hardware_protocol";
$TB_PROTOCOL            = "${core}protocol";
$TB_PROTOCOL_TYPE       = "${core}protocol_type";
$TB_SHORT_URL           = "${core}short_url";

$TB_MGED_ONTOLOGY_RELATIONSHIP  = $DBPREFIX{BioLink}."MGEDOntologyRelationship";
$TB_MGED_ONTOLOGY_TERM          = $DBPREFIX{BioLink}."MGEDOntologyTerm";
$TB_ONTOLOGY_RELATIONSHIP_TYPE  = $DBPREFIX{BioLink}."OntologyRelationshipType";
$TB_ONTOLOGY_TERM_TYPE          = $DBPREFIX{BioLink}."OntologyTermType";

$TB_TEST_PROTOCOL               = ${core}."test_protocol";
$TB_TEST_SAMPLE                 = ${core}."test_sample";
$TB_TEST_SAMPLE_PROTOCOL        = ${core}."test_sample_protocol";

$TB_PROJECT_FILE                = "${core}project_file";


###############################################################################

1;

__END__

###############################################################################
###############################################################################
###############################################################################

=head1 SBEAMS::Connection::Tables

SBEAMS Core table definitions

=head2 SYNOPSIS

See SBEAMS::Connection for usage synopsis.

=head2 DESCRIPTION

This pm defines the physical table names for the abstract table variables.


=head2 METHODS

=over

=item * none



=back

=head2 BUGS

Please send bug reports to the author

=head2 AUTHOR

Eric Deutsch <edeutsch@systemsbiology.org>

=head2 SEE ALSO

SBEAMS::Connection

=cut

