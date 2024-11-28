import random

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
        if self.shuffle:
            shuffled_queue = random.sample(self.queue, len(self.queue))
            self.current_index = 0
            print(f"Playing: {shuffled_queue[self.current_index]}")
        elif self.current_index is None:
            print("No track is currently playing.")
        else:
            print(f"Playing: {self.queue[self.current_index]}")


    def skip(self):
        if self.current is None:
            print("No track is currently playing.")
            return
        
        if self.current.next is None and not self.repeat:
            print("End of the queue. No more tracks to skip to.")
            return
        
        if self.repeat:
            self.current = self.list.head.track
            print(f"Playing: {self.current}")
        else:
            self.current = self.current.next.track if self.current.next else None
            if self.current:
                print(f"Playing: {self.current}")
            else:
                print("End of the queue.")

    def previous(self):
        if self.current is None:
            print("No track is currently playing.")
            return
        
        if self.current.prev is None:
            print("No previous track. You are at the start of the queue.")
            return
        
        self.current = self.current.prev.track
        print(f"Playing: {self.current}")

    def toggle_shuffle(self):
        self.shuffle = not self.shuffle
        status = "enabled" if self.shuffle else "disabled"
        print(f"Shuffle is now {status}.")

    def toggle_repeat(self):
        pass
    
    def add_tracks(self, new_tracks):
        pass
    
    def display_queue(self):
        pass
    
    def exit(self):
        pass