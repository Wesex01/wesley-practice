# This program writes three lines of data to a file.
# Open a file named 6-1-philosophers.txt.
def main():
    # Open a file named 6-1-philosophers.txt in write mode ('w').
    outfile = open('task1.txt', 'w')

    # Write the names of three philosophers to the file.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Close the file.
    outfile.close()

# Call the main function if the script is run directly.
if __name__ == "__main__":
    main()
