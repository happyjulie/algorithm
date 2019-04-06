#!/bin/python
# encoding: utf-8
# still wrong answer in edge case
# https://www.hackerrank.com/challenges/dijkstrashortreach/problem?h_r=internal-search&isFullScreen=false

import math
import os
import random
import re
import sys

from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    self.distances[(to_node, from_node)] = distance

# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    g = Graph()
    for edge in edges:
        g.add_edge(edge[0], edge[1], edge[2])
    #g.edges
    #g.distances

    initial_node = s
    visited={initial_node:0}
    path={}
    nodes = set(n+1 for n in range(n))
    #set type

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node]<visited[min_node]:
                    min_node = node

        if min_node is None:
            print 'min_node is none'
            break
 
        current_weight=visited[min_node]        
        nodes.remove(min_node)

        for edge in g.edges[min_node]:
            wt = current_weight + g.distances[(min_node, edge)]
            if edge not in visited or wt < visited[edge]:
                visited[edge]=wt
                path[edge]=min_node

    visited_list=[]
    for i in range(n):
        i=i+1
        if i != initial_node :
            if i in visited.keys():
                visited_list.append(visited[i])
            else:
                visited_list.append(-1)

    print visited_list        
    return visited_list
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        nm = raw_input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in xrange(m):
            edges.append(map(int, raw_input().rstrip().split()))

        s = int(raw_input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
