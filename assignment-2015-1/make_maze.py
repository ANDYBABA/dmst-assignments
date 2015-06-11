import argparse, random
def parse_args():
    optionparser = argparse.ArgumentParser()
    optionparser.add_argument('n', type=int)
    optionparser.add_argument('start_x', type=int)
    optionparser.add_argument('start_y', type=int)    
    optionparser.add_argument('input_seed')    
    optionparser.add_argument('output')
    args= optionparser.parse_args()    
    return args.n,args.start_x,args.start_y,args.input_seed,args.output


def make_maze(n,start_x,start_y,nodevisited):
    possiblenode=True
    while(possiblenode==True):
        nodes=find_neighbours(n, start_x, start_y)
        random_nodes = random.sample(nodes, len(nodes))
        possiblenode=False
        for neighbour in random_nodes:
            second_x, second_y =neighbour
            if nodevisited[second_x][second_y]==False:
                output_file.write("(%d, %d), (%d, %d)\n" %(start_x,start_y,second_x,second_y))
                start_x=second_x
                start_y=second_y
                nodevisited[second_x][second_y]=True
                possiblenode=True
                break;
            else:
                possiblenode=False
    return nodevisited

def find_neighbours(size,x,y):
    nodes = []
    if x-1 >= 0 : nodes.append((x-1,y))
    if y-1 >= 0 : nodes.append((x,y-1))
    if x+1 < size: nodes.append((x+1,y))
    if y+1 < size: nodes.append((x,y+1))
    return nodes

def all (size,values):
    for i in range(size):
        for j in range(size):
            if not(nodevisited[i][j]):
                return False
    return True

if __name__ == '__main__':
    n,start_x,start_y,input_seed,output= parse_args()
    output_file = open(output, "w")
    if (start_y>=n or start_y<0) or (start_x>=n or start_x<0):
        print ("The parameters you have given me are out of bounds.")
    else:
        nodevisited= [[False for i in range(n)] for j in range(n)]
        random.seed(input_seed)        
        nodevisited[start_x][start_y]=True
        nodevisited=make_maze(n, start_x, start_y,nodevisited)
        allnodevisited=all(n,nodevisited)
        while (allnodevisited==False):
            nodevisitednodes =[]
            for i in range(n):
                for j in range(n):
                    if nodevisited[i][j]==True:
                        nodevisitednodes.append((i,j))            
            random_nodevisited=random.sample(nodevisitednodes,len(nodevisitednodes))
            for nodevisited_node in random_nodevisited:
                start_x,start_y= nodevisited_node
                nodevisited=make_maze(n, start_x, start_y,nodevisited)
            allnodevisited=all(n,nodevisited)  
        output_file.close()            
 
