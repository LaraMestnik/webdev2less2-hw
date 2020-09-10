from smartninja_sql.sqlite import SQLiteDatabase

chinook = SQLiteDatabase("Chinook_Sqlite.sqlite")

chinook.print_tables(verbose=True)

chinook.pretty_print("SELECT * FROM Invoice;")
chinook.pretty_print("SELECT * FROM Customer;")

chinook.pretty_print("""SELECT Customer.FirstName, Customer.LastName, MAX(Invoice.Total)
                        FROM Invoice 
                        INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId;""")

chinook.pretty_print("""SELECT Customer.FirstName, Customer.LastName, MIN(Invoice.Total)
                        FROM Invoice 
                        INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId;
""")

chinook.pretty_print("""SELECT Invoice.BillingCity, COUNT(*) AS Invoice_num
                        FROM Invoice
                        GROUP BY Invoice.BillingCity
                        ORDER BY Invoice_num DESC;
""")


chinook.pretty_print("SELECT * FROM MediaType;")


chinook.pretty_print("""SELECT COUNT(*) FROM Track
                        INNER JOIN MediaType ON MediaType.MediaTypeId=Track.MediaTypeId
                        WHERE MediaType.Name='Protected AAC audio file';""")

chinook.pretty_print("""SELECT Artist.Name, COUNT(*) AS Album_num
                        FROM Artist
                        INNER JOIN Album ON Artist.ArtistId=Album.ArtistId
                        GROUP BY Album.ArtistId
                        ORDER BY Album_num DESC;
                        """)


chinook.pretty_print("""SELECT Genre.Name, COUNT(*) AS Track_count
                        FROM Genre
                        INNER JOIN Track ON Track.GenreId=Genre.GenreId
                        GROUP BY Track.GenreId
                        ORDER BY Track_count DESC;    
                            """)

chinook.pretty_print("""SELECT Customer.Firstname, Customer.LastName, SUM(Invoice.Total) AS Customer_total
                        FROM Customer
                        INNER JOIN Invoice ON Invoice.CustomerId=Customer.CustomerId
                        GROUP BY Customer.CustomerId
                        ORDER BY Customer_total DESC;
""")

chinook.pretty_print("""SELECT Invoice.InvoiceId, Track.Name
                        FROM Invoice
                        JOIN InvoiceLine ON InvoiceLine.InvoiceId = Invoice.InvoiceId
                        JOIN Track ON InvoiceLine.TrackId = Track.TrackId;
""")


