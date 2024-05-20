import hashlib

print("Welcome to the Voting System!")

# List of candidates with unique identifiers
candidates = {
    "1": "Alice",
    "2": "Bob",
    "3": "Charlie"
}

# Create an empty dictionary to store votes
votes = {}

def hash_vote(name, candidate_id):
    # Hash the voter's name and candidate ID using SHA-256 algorithm
    vote = f"{name}:{candidate_id}"
    hashed_vote = hashlib.sha256(vote.encode()).hexdigest()
    return hashed_vote

# Main loop for the voting system program
while True:
    # Display the menu options
    print("\nPlease choose an option:")
    print("1. Vote for a candidate")
    print("2. View voting results")
    print("3. Quit")
    
    # Prompt the user to choose an action
    choice = input("Enter your choice (1/2/3): ")
    
    # Voting for a candidate
    if choice == '1':
        # Display the list of candidates
        print("\nAvailable candidates:")
        for candidate_id, candidate_name in candidates.items():
            print(f"{candidate_id}. {candidate_name}")
        
        # Ask the user to enter their name and the candidate ID
        name = input("Enter your name: ")
        candidate_id = input("Enter the candidate ID you wish to vote for: ")
        
        if candidate_id not in candidates:
            print("Invalid candidate ID. Please try again.")
        else:
            secure_vote = hash_vote(name, candidate_id)
            if candidate_id in votes:
                votes[candidate_id].append(secure_vote)
            else:
                votes[candidate_id] = [secure_vote]
            print("Thank you for voting!")
    
    # Viewing voting results
    elif choice == '2':
        print("\nVoting Results:")
        if not votes:
            print("No votes have been cast yet.")
        else:
            for candidate_id, candidate_name in candidates.items():
                vote_count = len(votes.get(candidate_id, []))
                print(f"{candidate_name}: {vote_count} votes")
    
    # Quitting the program
    elif choice == '3':
        print("Thank you for using the Voting System. Goodbye!")
        break
    
    # Handling incorrect inputs
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
