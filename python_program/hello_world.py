# Hello, World!: Print "Hello, World!" to the console.
class HelloWorld:
    def __init__(self) -> None:
        self.text = "Hello, World!"

    # The __str__() method returns a human-readable 
    # or informal, string representation of an object.
    def __str__(self) -> str:
        return "%s" % self.text
    
message = HelloWorld()
print(message)