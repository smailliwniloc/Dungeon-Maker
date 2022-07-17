import logging
logging.basicConfig(filename='main.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

print("is this running?")

try:
    print("entering try")

    import project.control as control

    print("imported stuff")

    def main():
        print("Initiating controller")
        controller = control.ApplicationController()
        controller.run()


    if __name__ == "__main__":
        print("entering if statement")
        main()

    print("did nothing I guess")

except Exception as e:
    print("in exception")
    logging.exception("caught at main")
    raise e  # personal choice, still want to see error in IDE