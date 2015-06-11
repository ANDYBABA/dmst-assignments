import sys,json

if __name__ == '__main__':
    if(len(sys.argv)>2):
        gender=str(sys.argv[1])
        input_file=str(sys.argv[2])
        if(len(sys.argv)>4):
            output_file=str(sys.argv[4])
            file = open(output_file, "w+")             
        else:
            output_file=None
        with open(input_file) as data:    
            rankings = json.load(data)
        listmen = sorted(rankings["men_rankings"].keys())
        listwomen = sorted(rankings["women_rankings"].keys())
        men_rankings=rankings["men_rankings"]
        women_rankings=rankings["women_rankings"]
        engaged={}
        if (gender=="-m"):
            free=listwomen
            while free:
                woman=free[0]
                del free[0]
                listwomen2=women_rankings[woman]
                man=listwomen2[0]
                del listwomen2[0]
                commited=engaged.get(man)
                if not commited:
                    engaged[man]=woman
                else:
                    listmen2=men_rankings[man]
                    if   listmen2.index(woman)<listmen2.index(commited):
                        engaged[man] = woman
                        if men_rankings[commited]:
                            free.append(commited)
                    else:
                        if listwomen:
                            free.append(woman)
            if(output_file!=None):
                file.write('{\n    ')
                file.write(',\n    '.join('\"%s\": \"%s\"' % partners for partners in sorted(engaged.items())))
                file.write('\n}')
                file.close()
            else:
                print('{')
                print(',  '.join('\"%s\": \"%s\"' % partners for partners in sorted(engaged.items())))
                print('}')                            
        elif (gender=="-w"):
            free=listmen
            while free:
                man=free[0]
                del free[0]
                listmen = men_rankings[man]
                woman = listmen[0]
                del listmen[0]
                commited = engaged.get(woman)
                if not commited:
                    engaged[woman] = man
                else:
                    listwomen = women_rankings[woman]
                    if   listwomen.index(man) < listwomen.index(commited):
                        engaged[woman] = man
                        if men_rankings[commited]:
                            free.append(commited)
                    else:
                        if listmen:
                            free.append(man)
            if(output_file!=None):
                file.write('{\n    ')
                file.write(',\n    '.join('\"%s\": \"%s\"' % partners for partners in sorted(engaged.items())))
                file.write('\n}')
                file.close()
            else:
                print('{')
                print(',  '.join('\"%s\": \"%s\"' % partners for partners in sorted(engaged.items())))
                print('}')                
    else:
        print ("py stable_marriage.py gender input_file -o O")
           
