n=int(input("Enter no.of messages:"))
data={}
for i in range(n):
    name,message=input().split(":")    
    if name in data:
        data[name].append(message)
    else:
        data[name]=[message]
print(data)
choice={
    1: 'Count total number of messages',
    2: 'Identify unique users in the chat',
    3: 'Count total words in the chat',
    4: 'Calculate avg words per message',
    5: 'Find the longest message sent',
    6: 'Find the most active user',
    7: 'Get message count for a specific user',
    8: 'Find the most frequently used word by a specific user',
    9: 'Retrieve the first and last message sent by a user',
    10: 'Check if a user is present in the chat',
    11: 'Find commonly repeated words',
    12: 'Identify the user with the longest average message length',
    13: 'Count how many messages mention a specific user',
    14: 'Remove duplicate messages',
    15: 'Sort messages alphabetically',
    16: 'Extract all questions asked in the chat',
    17: 'Calculate the reply ratio between two users',
    18: 'Check for deleted messages',
    19: 'Exit'
}
for i,j in choice.items():
    print(f"Choice:{i}{j}")
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        print("Total messages:", n)
    elif ch==2:
        print("Unique users:", list(data.keys()))
    elif ch==3:
        total_words=sum(len(message.split()) for messages in data.values() for message in messages)
        print("Total words in chat:", total_words)
    elif ch==4:
        avg_words=total_words/n
        print(f"Average words per message:{avg_words}")
    elif ch==5:
        longest_message=max((message for messages in data.values() for message in messages), key=len)
        print("Longest message sent:", longest_message)
    elif ch==6:
        most_active_user=max(data, key=lambda user: len(data[user]))
        print("Most active user:", most_active_user)
    elif ch==7:
        s=input()
        if s in data:
            print(len(data[s]))
        else:
            print("User not found")
    elif ch==8:
        s=input()
        if s in data:
            from collections import Counter
            words=[word for message in data[s] for word in message.split()]
            most_common=Counter(words).most_common(1)
            print("Most frequently used word by", s, ":", most_common[0][0] if most_common else "No messages")
    elif ch==9:
        s=input()
        if s in data:
            print(f'First Message:{s}:{data[s][0]}')
            print(f'Last Message:{s}:{data[s][-1]}')
        else:
            print("No such name")
    elif ch==10:
        s=input()
        if s in data:
            print(f"{s} is present in the chat")
        else:
            print(f"{s} is not found in the chat")
    elif ch==11:
        from collections import Counter
        words=[word for i in data.values()  for msg in i for word in msg.split()]
        common_words=Counter(words).most_common()
        repeated_words=[word for word, count in common_words if count>1]
        print(f'common repeated words:{repeated_words}')
    elif ch==12:
        avg={user: sum(len(msg) for msg in msgs)/len(msgs) for user, msgs in data.items()}
        longest_avg_user=max(avg, key=avg.get)
        print(f'User with longest average message length:{longest_avg_user}')
    elif ch==13:
        s=input()
        count=sum(1 for msgs in data.values() for msg in msgs if s in msg)
        print(f'Messages mentioning {s}:{count}')
    elif ch==14:
        unique_meassaages=set(msg for msgs in data.values() for msg in msgs)
        print(f'Unique messages:{unique_meassaages}')
    elif ch==15:
        sorted_messages=sorted(msg for msgs in data.values() for msg in msgs)
        print(f'Sorted messages:{sorted_messages}')
    elif ch==16:
        questions=[msg for msgs in data.values() for msg in msgs if msg.endswith('?')]
        print(f'Questions in chat:{questions}')
    elif ch==17:
        user1=input("Enter first user:")
        user2=input("Enter second user:")
        replies = sum(1 for msg in data.get(user2, []) if user1 in msg)
        print(f'Reply ratio between {user1} and {user2}: {replies}')
    elif ch==18:
        if "" in (msg for msgs in data.values() for msg in msgs):
            print("There are deleted messages in the chat")
        else:
            print("No deleted messages found")
    elif ch==19:
        print("Exit")
        break

#OUTPUT:-

##Enter no.of messages:4
##praveen : hai
##kumar : hello
##praveen : how are you
##kumar : i am good what about you
##{'praveen ': [' hai', ' how are you'], 'kumar ': [' hello', ' i am good what about you']}
##Choice:1Count total number of messages
##Choice:2Identify unique users in the chat
##Choice:3Count total words in the chat
##Choice:4Calculate avg words per message
##Choice:5Find the longest message sent
##Choice:6Find the most active user
##Choice:7Get message count for a specific user
##Choice:8Find the most frequently used word by a specific user
##Choice:9Retrieve the first and last message sent by a user
##Choice:10Check if a user is present in the chat
##Choice:11Find commonly repeated words
##Choice:12Identify the user with the longest average message length
##Choice:13Count how many messages mention a specific user
##Choice:14Remove duplicate messages
##Choice:15Sort messages alphabetically
##Choice:16Extract all questions asked in the chat
##Choice:17Calculate the reply ratio between two users
##Choice:18Check for deleted messages
##Choice:19Exit
##Enter your choice:1
##Total messages: 4
##Enter your choice:2
##Unique users: ['praveen ', 'kumar ']
##Enter your choice:3
##Total words in chat: 11
##Enter your choice:4
##Average words per message:2.75
##Enter your choice:5
##Longest message sent:  i am good what about you
##Enter your choice:6
##Most active user: praveen 
##Enter your choice:7
##praveen
##User not found
##Enter your choice:7
##kumar 
##2
##Enter your choice:8
##kumar
##Enter your choice:8
##praveen 
##Most frequently used word by praveen  : hai
##Enter your choice:9
##praveen 
##First Message:praveen : hai
##Last Message:praveen : how are you
##Enter your choice:10
##kumar 
##kumar  is present in the chat
##Enter your choice:11
##common repeated words:['you']
##Enter your choice:12
##User with longest average message length:kumar 
##Enter your choice:13
##praveen 
##Messages mentioning praveen :0
##Enter your choice:14
##Unique messages:{' hello', ' i am good what about you', ' hai', ' how are you'}
##Enter your choice:15
##Sorted messages:[' hai', ' hello', ' how are you', ' i am good what about you']
##Enter your choice:16
##Questions in chat:[]
##Enter your choice:17
##Enter first user:praveen
##Enter second user:kumar
##Reply ratio between praveen and kumar: 0
##Enter your choice:18
##No deleted messages found
##Enter your choice:19
##Exit