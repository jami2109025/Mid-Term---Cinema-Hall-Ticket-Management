class Hall:
    def __init__(self, rows, columns, hall_no) -> None:
        self.__rows = rows
        self.__columns = columns
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []

        for row in range(rows):
            for column in range(columns):
                self.__seats[(row, column)] = 'Vacant'

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)

        seat_allocation = []
        for row in range(self.__rows):
            seat_allocation.append(['Vacant'] * self.__columns)

        self.__seats[id] = seat_allocation

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print(f"Show with {show_id} id does not exist")
            return
        
        for row, column in seat_list:
            if row >= 0 and row < self.__rows and column >= 0 and column < self.__columns:
                if self.__seats[show_id][row][column] == 'Vacant':
                    self.__seats[show_id][row][column] = 'Booked'
                    print(f'Seat at row {row} and column {column} is booked successfully.')
                else:
                    print(f'Seat at row {row} and column {column} is already booked.')
            else:
                print("Invalid seat!!!")

    def get_show_list(self):
        return self.__show_list
    
    def get_available_seats(self, show_id):
        if show_id not in self.__seats:
            print(f'Show with id-{show_id} does not exist. ')
            return None
        
        available_seats = []
        for row in range(self.__rows):
            for column in range(self.__columns):
                if self.__seats[show_id][row][column] == 'Vacant':
                    available_seats.append((row, column))
        return available_seats

    def view_show_list(self):
        print("Show running in the hall: ")
        for show_info in self.__show_list:
            print(f'Show ID: {show_info[0]}, Movie : {show_info[1]},Time : {show_info[2]}')

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print(f'Show with id-{show_id} does not exist. ')
            return
        print(f'Available seats for show with id-{show_id}: ')
        for row in range(self.__rows):
            for column in range(self.__columns):
                if self.__seats[show_id][row][column] == 'Vacant':
                    print(f'Row :{row}, Column :{column}')


def ticket_counter():
    hall = Hall(rows=15, columns=12, hall_no=1)

    while True:
        print('\nWelcome to the Ticket Counter...')
        print('1. View all running shows')
        print('2. View available seats for a show')
        print('3. Book tickets for a show')
        print('4. Exit')

        choice = input("Enter your choice: ")

        if choice == '1':
            hall.view_show_list()
        elif choice == '2':
            show_id = int(input("Enter the show id: "))
            available_seats = hall.get_available_seats(show_id)
            if available_seats:
                print(f'Available seats for show with id-{show_id}: ')
                for row, column in available_seats:
                    print(f'Row :{row}, Column :{column}')
        elif choice == '3':
            show_id = int(input("Enter the show id: "))
            
            seat_input = input("Enter seat row and column separated by space (e.g., '2 3'): ")
            seat_values = seat_input.split()
            if len(seat_values) != 2:
                print("Error: Please provide both row and column values separated by space.")
                continue

            try:
                row, column = map(int, seat_values)
            except ValueError:
                print("Error: Please provide valid integers for row and column.")
                continue
            
            available_seats = hall.get_available_seats(show_id)
            if not available_seats:
                print(f"No available seats for show with id-{show_id}.")
                continue
            
            if (row, column) not in available_seats:
                print('Error: Invalid seat!!')
                continue

            if hall._Hall__seats[show_id][row][column] == 'Booked':
                print('Error: Seat you selected is already booked!')
            else:
                hall.book_seats(show_id, [(row, column)])

        elif choice == '4':
            print("Hope you will enjoy your day")
            break
        else:
            print('Invalid choice. Please enter a valid choice...')

ticket_counter()
