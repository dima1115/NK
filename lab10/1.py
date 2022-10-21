#import os
#x = open("story.txt", "w")
#x.write("To Sherlock Holmes she is always THE woman. I have seldom heard him mention her under any other name. In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler. All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind. He was, I take it, the most perfect reasoning and observing machine that the world has seen, but as a lover he would have placed himself in a false position. He never spoke of the softer passions, save with a gibe and a sneer. They were admirable things for the observer—excellent for drawing the veil from men’s motives and actions.")
import re

x = open("story.txt", "r")
z=x.read()
result = len(re.findall(r'\w+', z))
M = {}
for key in z.split():
    M[key] = M.setdefault(key, 0) +1
m = open("words.txt", "w")
m.write(str(result))
m.write(" ")
m.write(str(len(M)))
m.write(" ")
m.write(str(len([i for i in z.split('. ')])))
x.close()
