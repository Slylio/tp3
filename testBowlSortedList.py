import Bowl
import BowlSortedList

# %% Test création bowl
bowl = Bowl.Bowl("blue")
print(bowl)

# %% Test création  SortedListOfBowls
sortedList=BowlSortedList.BowlSortedList()
sortedList.init_bowls(4)
print(sortedList)
#%% Test insert_bowl
sortedList.insert_bowl(bowl)
print(sortedList)

#%%Test count_color
print("number of reds : "+str(sortedList.count_color("red")))

#%% Test first_bowl
print("position of first blue : "+str(sortedList.first_bowl("blue")))

#%% Test keme_bowl
print("position of 2nd blue : "+str(sortedList.keme_bowl(2,"blue")))

#%% Test delete_bowls
sortedList.delete_bows("red")
print("After deleting red bowls : "+ str(sortedList))