class PropertyUtil:
    @staticmethod
    def getPropertyString():
        # Read connection details from a property file
        # property file is named 'db_properties.txt' and contains key-value pairs for hostname, dbname
        properties = {}
        with open('db_properties.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                properties[key.strip()] = value.strip()

        # Construct the connection string
        connection_string = f"DRIVER={{SQL Server}};SERVER={properties['hostname']};DATABASE={properties['dbname']};Trusted_Connection=yes"
        return connection_string

