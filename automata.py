# A template file for your solution. 
# You are not allowed to use python libraries.
# Make sure to give good comments that explain your solution.

# You must define: 
# a DFA that accepts strings containing an even number of 1s;
# a DFA that accepts strings that contain the substring "1010"; and 
# a DFA that accepts strings that contain at least three 0's, at least three 1's, and end with '0011'.

# You can use maps to encode DFAs.


"""3 Functions which take in a deterministic finite state automaton and a string and check whether it is accepted by the DFA."""


def check_acceptance(dfa, string):
    
    """state is set to the starting state of the DFA. We then loop through the string and adjust the state based on the input.
    If the string has been accepted, the state will be equal to the final state at the end of the loop. We return the boolean value."""

    state = dfa["start"]

    for i in string:
        state = dfa["transition"][state][i]
    
    return state in dfa["accept"]




def fa1(string):

    """The transition here checks for an even number of 1s before arriving at the final state."""
    
    dfa_1 = {
        'start': 'A',
        'accept': {'A'},
        'transition': {
        'A': {'0': 'A', '1': 'B'},
        'B': {'0': 'B', '1': 'A'},
         }
        }

    return check_acceptance(dfa_1, string)


def fa2(string):

    """Here the transition checks for the substring 0101 before arriving at the final state"""

    dfa_2 = {
        'start': 'A',
        'accept': {'E'},
        'transition': {
        'A': {'0': 'A', '1': 'B'},
        'B': {'0': 'C', '1': 'B'},
        'C': {'0': 'A', '1': 'D'},
        'D': {'0': 'E', '1': 'B'},
        'E': {'0': 'E', '1': 'E'}
        }
         }

    return check_acceptance(dfa_2, string) 


def fa3(string):
    
    """Here the transition checks for at least one 0 and one 1 before an ending 0011 after which we arrive at the final state.
    This guarantees at least three 0s and three 1s."""

    dfa_3 = {
        'start': 'A',
        'accept': {'G'},
        'transition': {
        'A': {'0': 'B', '1': 'C'},
        'B': {'0': 'B', '1': 'D'},
        'C': {'0': 'D', '1': 'C'},
        'D': {'0': 'E', '1': 'D'},
        'E': {'0': 'F', '1': 'D'},
        'F': {'0': 'F', '1': 'G'},
        'G': {'0': 'E', '1': 'H'},
        'H': {'0': 'E', '1': 'D'}
        }
     }
    
    return check_acceptance(dfa_3, string) 


