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

class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __repr__(self):
        return f"{self.title} - {self.artist} ({self.duration // 60}:{self.duration % 60:02d})"


class Queues:
    def __init__(self):
        self.list = List()
        self.current = None
        self.shuffle = False
        self.repeat = False
        self.paganation = 10
        self.originalOrder = []
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
        if self.shuffle:
            print("Disabling shuffle mode.")
            self.shuffle = False
        self.repeat = not self.repeat
        print(f"Repeat mode is now {'On' if self.repeat else 'Off'}.")
    
    def add_tracks(self, new_tracks):
        for track in new_tracks:
            self.list.append(track)
        if not self.current:
            self.current = self.list.head
        self.update_duration()
    
    def display_queue(self):
        print(f"Total Duration: {self.total_duration // 3600} hr {self.total_duration % 3600 // 60} min")
        print(f"Shuffle: {'Shuffle On' if self.shuffle else 'Shuffle Off'}")
        print(f"Repeat: {'Repeat On' if self.repeat else 'Repeat Off'}")
        print("Tracks:")
        current = self.list.head
        index = 0
        page = 1
        trackCount = 1
        while current:
            if trackCount == self.paganation:
                print(f"Page {page}:")
                input("Press Enter to view the next page ")
                trackCount = 0
                page += 1

            prefix = "(Currently Playing)" if current == self.current else f"({index + 1})"
            print(f"{prefix}{current.track.title} - {current.track.artist} ({current.track.duration})")
            current = current.next
            index += 1
            trackCount += 1

        if trackCount > 0:
            print(f"Page {page}:")
            
    def load_queue(self):
        try: 
            with open('queue.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                    if len(parts) !=3:
                        print("Skipping Invalid")
                        continue

                title, artist, duration = line.strip().split(', ')
                track = Track(title, artist, int(duration))
                self.list.append(track)
                self.original_order.append(track)
                self.total_duration += int(duration)

            print("Queue is loaded.")
        except FileNotFoundError:
            print("No saved queue.")

    def exit(self):
        self.save_queue()
        print("Queue saved.")


    def queue_menu(self):
        while True:
            print("\nQueue Menu:")
            print("[1] Play")
            print("[2] Skip")
            print("[3] Previous")
            print("[4] Toggle Repeat")
            print("[5] Toggle Shuffle")
            print("[6] Display Queue")
            print("[7] Exit Queue Interface")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.play()
            elif choice == "2":
                self.skip()
            elif choice == "3":
                self.previous()
            elif choice == "4":
                self.toggle_repeat()
            elif choice == "5":
                self.toggle_shuffle()
            elif choice == "6":
                self.display_queue()
            elif choice == "7":
                self.exit()
                break
            else:
                print("Invalid choice. Please try again.")

        