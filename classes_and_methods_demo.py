# Demonstrate Python Classes and Methods

class Server:
    # Class attribute (shared by all instances)
    category = "Kubernetes Node"

    # Constructor (called when you create a new instance)
    def __init__(self, name, cpu, memory):
        # Instance attributes (unique per object)
        self.name = name
        self.cpu = cpu
        self.memory = memory
        print(f"✅ Created server '{self.name}' with {self.cpu} CPU and {self.memory}GB RAM.")

    # Instance method (acts on one specific object)
    def describe(self):
        return f"Server {self.name}: {self.cpu} CPU, {self.memory}GB RAM"

    # Instance method that modifies the object
    def upgrade(self, cpu_increase):
        self.cpu += cpu_increase
        print(f"🔧 Upgraded {self.name} → now has {self.cpu} CPU cores.")

    # Class method (acts on the class itself, not individual instances)
    @classmethod
    def info(cls):
        print(f"ℹ️  This class represents {cls.category}s in the cluster.")

    # Static method (utility function; doesn't access instance or class directly)
    @staticmethod
    def is_valid_memory(memory_value):
        return memory_value > 0


# --------------------------
# Demonstration
# --------------------------
def main():
    print("=== CLASS AND METHODS DEMO ===\n")

    # Access class method without creating an object
    Server.info()

    # Create two server objects
    node1 = Server("pool-mailer", 4, 8)
    node2 = Server("pool-monitor", 2, 4)

    # Call instance methods
    print(node1.describe())
    print(node2.describe())

    # Modify an instance
    node1.upgrade(2)

    # Static method example
    print("Memory check:", Server.is_valid_memory(0))   # False
    print("Memory check:", Server.is_valid_memory(16))  # True

    # Show instance attributes
    print("\nNode1:", node1.__dict__)
    print("Node2:", node2.__dict__)

if __name__ == "__main__":
    main()