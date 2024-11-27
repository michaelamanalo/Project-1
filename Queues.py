class Node:
    def __init__(self, track):
        self.track = track
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, track):
        new_node = Node(track)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def remove_list(self):
        self.head = None
        self.tail = None
        self.size = 0



class Queues:
    def __init__(self):
        self.list = List()
        self.current = None
        self.shuffle = False
        self.repeat = False
        self.paganation = 10
        self.total_duration = 0

    def play(self):
        # Play current track
        pass
    
    def skip(self):
        # Move to next track
        pass
    
    def previous(self):
        # Move to previous track
        pass
    
    def toggle_shuffle(self):
        # Toggle shuffle state
        pass
    
    def toggle_repeat(self):
        # Toggle repeat state
        pass
    
    def add_tracks(self, new_tracks):
        # Add new tracks to the queue
        pass
    
    def display_queue(self):
        # Display the queue with pagination and other stats
        pass
    
    def exit(self):
        # Exit and save the state of the queue
        pass

    



