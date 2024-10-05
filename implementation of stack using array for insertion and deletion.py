class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {value} to stack")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None
        popped_value = self.top.value
        self.top = self.top.next
        print(f"Popped {popped_value} from stack")
        return popped_value

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        current = self.top
        print("Stack:", end=" ")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()
print(f"Top element is {stack.peek()}")
stack.pop()
stack.print_stack()
print(f"Top element is {stack.peek()}")
