class TicketBooking:
    def __init__(self):
        self.total_tickets = 100
        self.booked_tickets = 0

    def book_ticket(self, num=1):
        if self.booked_tickets + num <= self.total_tickets:
            self.booked_tickets += num
            print(f"{num} tickets booked successfully!")
        else:
            print("Not enough tickets available.")

    def available_tickets(self):
        return self.total_tickets - self.booked_tickets

    def booked_count(self):
        return self.booked_tickets

system = TicketBooking()

system.book_ticket(3)   
system.book_ticket(5)   
system.book_ticket(4)   
print("Booked tickets:", system.booked_count())
print("Available tickets:", system.available_tickets())
           

        
