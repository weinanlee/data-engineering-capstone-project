class SqlQueries:
    table_name = ['staging_immigration','immigration', 'i94cit_i94res', 'i94mode','i94addr','i94visa','i94port']


    staging_immigrant_table_create = """
    CREATE TABLE IF NOT EXISTS public.staging_immigration (
        Unnamed       INT,
        cicid         FLOAT,
        i94yr         FLOAT,
        i94mon        FLOAT,
        i94cit        FLOAT,
        i94res        FLOAT,
        i94port       VARCHAR,
        arrdate       FLOAT,
        i94mode       FLOAT,
        i94addr       VARCHAR,
        depdate       FLOAT,
        i94bir        FLOAT,
        i94visa       FLOAT,
        count         FLOAT,
        dtadfile      INT,
        visapost      VARCHAR,
        occup         VARCHAR,
        entdepa       VARCHAR,
        entdepd       VARCHAR,
        entdepu       FLOAT,
        matflag       VARCHAR,
        biryear       FLOAT,
        dtaddto       VARCHAR,
        gender        VARCHAR,
        insnum        FLOAT,
        airline       VARCHAR,
        admnum        FLOAT,
        fltno         VARCHAR,
        visatype      VARCHAR)
    
    """

    drop_table = """
    DROP TABLE IF EXISTS {};
    """
    immigrant_table_create = """CREATE TABLE IF NOT EXISTS public.immigration (
        cicid FLOAT PRIMARY KEY,
        i94yr FLOAT,
        i94mon FLOAT,
        i94cit FLOAT,
        i94res FLOAT,
        i94port VARCHAR,
        arrdate FLOAT,
        i94mode FLOAT,
        i94addr VARCHAR,
        depdate FLOAT,
        i94bir FLOAT,
        i94visa FLOAT,
        count FLOAT,
        dtadfile VARCHAR,
        visapost VARCHAR,
        occup VARCHAR,
        entdepa VARCHAR,
        entdepd VARCHAR,
        entdepu VARCHAR,
        matflag VARCHAR,
        biryear FLOAT,
        dtaddto VARCHAR,
        gender VARCHAR,
        insnum VARCHAR,
        airline VARCHAR,
        admnum FLOAT,
        fltno VARCHAR,
        visatype VARCHAR
        );
    """
    ## I94CIT & I94RES - This format shows all the valid and invalid codes for processing 
    i94cit_i94res_table_create = """
    CREATE TABLE IF NOT EXISTS public.i94cit_i94res (
        code SMALLINT PRIMARY KEY,
        country VARCHAR
        );
    """
    
 #    port_of_entry_codes_table_create = """
 #    """

    ## /* I94PORT - This format shows all the valid and invalid codes for processing */
    i94port_table_create = """
    CREATE TABLE IF NOT EXISTS public.i94port (
            code VARCHAR PRIMARY KEY,
            port_of_entry VARCHAR,
            city VARCHAR,
            state_or_country VARCHAR
        );
    """

    ## I94MODE - There are missing values as well as not reported (9)
    i94mode_table_create = """
    CREATE TABLE IF NOT EXISTS public.i94mode (
        code SMALLINT PRIMARY KEY,
        transportation VARCHAR
        );
    """

    ## I94ADDR - There is lots of invalid codes in this variable and the list below 
    ## shows what we have found to be valid, everything else goes into 'other'
    i94addr_table_create = """
    CREATE TABLE IF NOT EXISTS public.i94addr (
        code VARCHAR PRIMARY KEY,
        state VARCHAR
        );
    """
    ## I94VISA - Visa codes collapsed into three categories:
    ## 1 = Business
    ## 2 = Pleasure
    ## 3 = Student
    i94visa_table_create = """
    CREATE TABLE IF NOT EXISTS public.i94visa (
        code SMALLINT PRIMARY KEY,
        reason_for_travel VARCHAR
        );
    """