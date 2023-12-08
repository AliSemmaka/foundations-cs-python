# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:26:12 2023

@author: alise
"""

#Exercise 1

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, city1, city2):
        self.graph[city1].append(city2)
        self.graph[city2].append(city1)

    def is_route_exists(self, start, end, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)

        if start == end:
            return True

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                if self.is_route_exists(neighbor, end, visited):
                    return True

        return False
    
    def print_reachable_cities(self, city):
        if city not in self.graph:
            print(f"No information available for {city}")
        else:
            print(f"Cities directly reachable from {city}: {', '.join(self.graph[city])}")
       

cities_graph = Graph()
cities_graph.add_edge("akkar", "beirut")
cities_graph.add_edge("beirut", "saida")
cities_graph.add_edge("saida", "sour")
cities_graph.add_edge("sour", "zahle")

# Get user input for two cities
start_city = input("Enter the starting city: ")
end_city = input("Enter the destination city: ")

#Test if a route exists
route_exists = cities_graph.is_route_exists(start_city, end_city)
print(f"There is a route between {start_city} and {end_city}: {route_exists}")

# Get user input for a city
selected_city = input("Enter a city to see directly reachable cities: ")

# Print directly reachable cities
cities_graph.print_reachable_cities(selected_city)




#Exercise 2

# from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, city1, city2):
        self.graph[city1].append(city2)

    def has_cycle_util(self, node, visited, recursion_stack):
        visited.add(node)
        recursion_stack.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.has_cycle_util(neighbor, visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(node)
        return False

    def has_cycle(self):
        visited = set()
        recursion_stack = set()

        for node in self.graph:
            if node not in visited:
                if self.has_cycle_util(node, visited, recursion_stack):
                    return True
        return False

cities_graph = Graph()
cities_graph.add_edge("akkar", "beirut")
cities_graph.add_edge("beirut", "saida")
cities_graph.add_edge("saida", "sour")
cities_graph.add_edge("sour", "zahle")
cities_graph.add_edge("zahle", "akkar")  # This creates a cycle

# Check if the graph has a cycle
if cities_graph.has_cycle():
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")




#Exercise 3

# from collections import defaultdict

class InstagramGraph:
    def __init__(self):
        self.graph = defaultdict(set)

    def add_follow(self, user1, user2):
        self.graph[user1].add(user2)
        self.graph[user2].add(user1)

    def common_followers(self, user1, user2):
        common_followers_list = list(self.graph[user1] & self.graph[user2])
        print(f"Common followers of {user1} and {user2}: {', '.join(common_followers_list)}")

    def no_followers(self, user1, user2):
        all_users = set(self.graph.keys())
        non_followers_list = list(all_users - (self.graph[user1] | self.graph[user2]))
        print(f"Users none of {user1} and {user2} follow: {', '.join(non_followers_list)}")

instagram_graph = InstagramGraph()

# Get user input for follow relationships
user1 = input("Enter the first user: ")
user2 = input("Enter the second user: ")

instagram_graph.add_follow("user1", "user2")
instagram_graph.add_follow("user1", "user3")
instagram_graph.add_follow("user2", "user4")
instagram_graph.add_follow("user3", "user4")
instagram_graph.add_follow("user5", "user6")

# Test common followers
instagram_graph.common_followers(user1, user2)

# Test users none of them follow
instagram_graph.no_followers(user1, user2)





