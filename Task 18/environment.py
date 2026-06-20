from utilities.driver_factory import DriverFactory

def before_scenario(context, scenario):
    print("=== Browser Started ===")
    context.driver = DriverFactory.get_driver()

def after_scenario(context, scenario):
    print("=== Browser Closed ===")
    context.driver.quit()