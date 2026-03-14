chai_menu=["masala","ginger","cardamom","tulsi"]
try:
    print(chai_menu[4])
except IndexError:
    print("Index out of bounds!")
    
chai_menu={"masala":150,"ginger":200,"cardamom":250,"tulsi":300}
try:
    print(chai_menu["elaichi"])
except KeyError:
    print("Key not found in the dictionary!") 
    
    
    
# try catch finally example
def serve_chai(chai_type):
    try:
        print(f"Serving a cup of {chai_type} chai")
        if chai_type not in chai_menu:
            raise ValueError("Chai type not available!")
    except ValueError as e:
        print(e)
    finally:
        print("Thank you for visiting our chai shop!")
serve_chai("elaichi")
serve_chai("masala")