import sys

class Node :
		def __init__(self, v) :
				self.data = v
				self.visited = False
				self.l = None
				self.r = None
		

class Tree :
		def __init__(self) :
				self.root = None
		
		def add(self, v) :
				if self.root != None :
						current = self.root
						while(True) :
								if current.data > v :
										if current.l == None :
												current.l = Node(v)
												break
										current = current.l
								elif current.data < v :
										if current.r == None :
												current.r = Node(v)
												break
										current = current.r
				else : 
						self.root = Node(v)

tree = Tree()

while True :
		try: 
				tree.add(int(input()))
		except:
				break

stack = [tree.root]
answer = []

while stack :
		node = stack.pop()
		answer.append(node.data)

		if node.l :
				stack.append(node.l)
		if node.r :
				stack.append(node.r)

while answer :
		sys.stdout.write(str(answer.pop()) + "\n")