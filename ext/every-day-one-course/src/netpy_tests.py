from lib import netpy
import time
import sys



def test_init():
    """
		Test the init function.
    """
    print("Testing the init function...")
    netpy.init()
    print("Done testing the init function.")

def test_check_connection():
	print("Testing the check.connection function...")
	if netpy.check.connection():
		print("You have internet connection.")
	else:
		print("You don't have internet connection.")
	print("Done testing the check.connection function.")

def test_check_ip():
	print("Testing the check.ip function...")
	print("Your public IP address is: " + netpy.check.ip())
	print("Done testing the check.ip function.")
 
def test_check_ip_info():
	print("Testing the check.ip_info function...")
	print("Your public IP address and some other information about your IP address is: " + str(netpy.check.ip_info()))
	print("Done testing the check.ip_info function.")
 
def test_server_start():
	print("Testing the server.start function...")
	try:
		server = netpy.server.start(3000)
		time.sleep(2)
		print("Server started on port 3000.")
		time.sleep(20)
		if server:
			netpy.server.stop(server)
		print("Done testing the server.start function.")
	except:
		print(netpy.Fore.RED + "Error: " + netpy.Fore.RESET + "The server.start function failed.")
		sys.exit(1)
 
def test_pyaxios_get():
	print("Testing the pyaxios.get function...")
	print("The response of the request is: " + str(netpy.pyaxios.get("https://api.ipify.org")))
	print("Done testing the pyaxios.get function.")
 
def test_all():	
	test_init()
	print("========================================")
	time.sleep(8)
	test_check_connection()
	print("========================================")
	time.sleep(8)
	test_check_ip()
	print("========================================")
	time.sleep(8)
	test_check_ip_info()
	print("========================================")
	time.sleep(8)
	test_server_start()
	print("========================================")
	time.sleep(8)
	test_pyaxios_get()
	print("========================================")
	time.sleep(8)
	print("Done testing all the functions." + netpy.Fore.GREEN + " [OK]" + netpy.Fore.RESET)
 
test_all()