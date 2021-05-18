def execption_handling():

    try:
        car = {"Make":"BMW", "Model":"500i","Year":"2021"}
        print(car[color])
    except:

        print("Exception occured")
        raise Exception()
    finally:
        print("Chutiya hai kuch nhi aata saale ko")

execption_handling()


