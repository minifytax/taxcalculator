def main():
    """
    """
    parser = optparse.OptionParser()
    
    # meta
    parser.add_option('--verbose', '-v', dest='verbose',
                      action="store_true",  
                      help="be verbose")
    parser.add_option('--doctest', '-t', dest='run_doctest', action="store_true", 
                      help="run doctests")


    options, positional_args = parser.parse_args()
    
    if options.verbose:
        log.setLevel(logging.DEBUG)
    
    if options.run_doctest:
        import doctest
        doctest.testmod()
        return 0
    
    source_directory, output_directory = positional_args if len(positional_args)==2 else (None, None)
    if not source_directory:
        parser.print_usage()
        return 1

    # @todo: FIXME - assumes relative location        
    schema_dir = os.path.join(os.path.dirname(__file__), '../schemas/ed-fi')
    schema_path = os.path.relpath(schema_dir, output_directory)

    if not os.path.isdir(output_directory):
        os.makedirs(output_directory)
                
    for csv_sources, xml_file_name, xml_file_class in (
           ([('student-sample-data.csv', Student_CSV_Reader)], 'InterchangeStudent.xml', Student_Interchange_File)
          ,([('lea-sample-data.csv', LEA_CSV_Reader), 
             ('school-sample-data.csv', School_CSV_Reader),
             ('course-sample-data.csv', Course_CSV_Reader),
             ('section-sample-data.csv', Section_CSV_Reader)], 'InterchangeSchool.xml', Ed_Org_Interchange_File)
         # ,('lea-sample-data.csv', Student_CSV_Reader, 'InterchangeLEA.xml', Student_Interchange_File)
          ,([('student-school-assoc-sample-data.csv', Student_School_Assoc_CSV_Reader),
             ('student-section-assoc-sample-data.csv', Student_Section_Assoc_CSV_Reader)], 'InterchangeEnrollment.xml', Enrollment_Interchange_File)
          ,([('staff-sample-data.csv', Staff_CSV_Reader), 
             ('teacher-school-assoc-sample-data.csv', Teacher_School_Assoc_CSV_Reader), 
             ('teacher-section-assoc-sample-data.csv', Teacher_Section_Assoc_CSV_Reader)], 'InterchangeStaffAssociation.xml', Staff_Assoc_Interchange_File)
           ):

        xml_file = xml_file_class(open(os.path.join(output_directory, xml_file_name), 'w'), schema_path) 
        
        try:
            for csv_file_name, csv_reader_class in csv_sources:
                csv_reader = csv_reader_class(open(os.path.join(source_directory, csv_file_name),'rU'))
                for xml_string in csv_reader.generate_xml_strings():
                    print >> xml_file, xml_string
        finally:
            xml_file.close()
            
    return 0
