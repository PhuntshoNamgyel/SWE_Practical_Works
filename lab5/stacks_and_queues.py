## Part 1: Implementing a Stack

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.size())  # Should print 2


## Part 2: Implementing a Queue

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.front())  # Should print 2
print(queue.size())  # Should print 2


## Part 3: Solving Practical Problems

# Problem 1: Balanced Parentheses

def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test the function
print(is_balanced("((()))"))  # Should print True
print(is_balanced("(()"))  # Should print False

# Problem 2: Reverse a String

def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test the function
print(reverse_string("Hello, World!"))  # Should print "!dlroW ,olleH"


# Problem 3: Hot Potato Simulation

def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

# Test the function
names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7))  # The winner's name will be printed


## EXERCISES ##

## Part 4: Implement a function that uses a stack to evaluate postfix expressions.

def evaluate_postfix(expression):
    stack = Stack()  # Initialize a stack to hold numbers during evaluation
    for token in expression.split():  # Split the expression into tokens
        if token.isdigit():  # If the token is a number
            stack.push(int(token))  # Convert it to an integer and push onto the stack
        else:  # The token is an operator
            b = stack.pop()  # Pop the top two numbers from the stack
            a = stack.pop()
            # Perform the appropriate operation based on the operator
            if token == '+':
                stack.push(a + b)  # Push the result back onto the stack
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)  # Division; note: this performs float division
    return stack.pop()  # The final result will be the last item on the stack

# Test the function
print(evaluate_postfix("3 2 + 7 * 7 /"))  # Should print 5.0


## Part 5: Implementing a Queue with Two Stacks

class TwoStackQueue:
    def __init__(self):
        self.stack1 = Stack()  # Stack to hold incoming elements
        self.stack2 = Stack()  # Stack to hold outgoing elements

    def enqueue(self, item):
        self.stack1.push(item)  # Push new items onto stack1

    def dequeue(self):
        # If stack2 is empty, transfer elements from stack1 to stack2
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        # If both stacks are empty, raise an error
        if self.stack2.is_empty():
            raise IndexError("Queue is empty")  # Raise an error if the queue is empty
        return self.stack2.pop()  # Pop the front item from stack2

    def is_empty(self):
        # The queue is empty if both stacks are empty
        return self.stack1.is_empty() and self.stack2.is_empty()

    def size(self):
        # Return the total number of items in the queue
        return self.stack1.size() + self.stack2.size()

# Test the TwoStackQueue
two_stack_queue = TwoStackQueue()
two_stack_queue.enqueue(1)
two_stack_queue.enqueue(2)
two_stack_queue.enqueue(3)
print(two_stack_queue.dequeue())  # Should print 1
print(two_stack_queue.size())      # Should print 2


## Part 6: Task Scheduler

class TaskScheduler:
    def __init__(self):
        self.task_queue = Queue()  # Initialize a queue to hold tasks

    def add_task(self, task):
        """Adds a task to the scheduler."""
        self.task_queue.enqueue(task)  # Enqueue the task

    def run_tasks(self):
        """Processes tasks in the order they were added."""
        while not self.task_queue.is_empty():  # Process until the queue is empty
            task = self.task_queue.dequeue()  # Dequeue the next task
            print(f"Processing task: {task}")  # Print the task being processed

# Test the TaskScheduler
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")
scheduler.run_tasks()  # Should process and print each task


## Part 7: Infix to Postfix Conversion

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}  # Define operator precedence
    stack = Stack()  # Initialize a stack for operators
    postfix_list = []  # List to hold the resulting postfix expression
    
    tokens = expression.split()  # Split the expression into tokens
    
    for token in tokens:
        if token.isalnum():  # If the token is an operand (numbers, letters)
            postfix_list.append(token)  # Add operands directly to the output list
        elif token == '(':  
            stack.push(token)  # Push onto the stack
        elif token == ')':  
            top_token = stack.pop()
            # Pop operators to the output list until left parenthesis is found
            while top_token != '(':
                postfix_list.append(top_token)  
                top_token = stack.pop()
        else:  # Operator
            # Pop higher or equal precedence operators from the stack to the output
            while (not stack.is_empty()) and (precedence[stack.peek()] >= precedence[token]):
                postfix_list.append(stack.pop())  
            stack.push(token)  # Push the current operator onto the stack
    
    # Pop any remaining operators in the stack to the output
    while not stack.is_empty():
        postfix_list.append(stack.pop())
    
    return " ".join(postfix_list)  # Join the postfix list into a string

# Test the function
print(infix_to_postfix("A + B * C"))  # Should print "A B C * +"
print(infix_to_postfix("( A + B ) * C - D"))  # Should print "A B + C * D -"
