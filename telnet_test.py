import telnetlib


def make_telnet_connection(url, port, time_out):
    """
    make requests using requests module in python.
    :param url:
    :param time_out:
    :return:
    """
    # logger.info("{} {} {} ".format(url, port , time_out))
    try:
        connection = telnetlib.Telnet(url, port, int(time_out))
        # logger.info("{} healthcheck successful".format(url))
        #return bool(connection)
    except:
        # logger.info("{} healthcheck failed".format(url))
        #return False
        print 'except'

    finally:
        print connection
        print connection.get_socket(), connection.fileno()
        return bool(connection)

make_telnet_connection('192.168.8.106', 8080, 2)
#print Telnet.get_socket()

connection_list = []
num = 0
while num <5:

    con = make_telnet_connection('192.168.8.106', 8080, 2)
    connection_list.append(con)
    num +=1

