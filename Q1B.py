def find_sums(target, current_sum=0, start=1):
    if current_sum == target:
        return 1
    if current_sum > target:
        return 0
    
    count = 0
    for i in range(start, 100):  # Adjust upper limit as necessary
        count += find_sums(target, current_sum + 1/(i*i), i + 1)
    return count

# Main function to invoke the solution
def main():
    target = 0.5
    result = find_sums(target)
    print(f"Number of ways to write 1/2 as a sum of inverse squares: {result}")

if __name__ == "__main__":
    main()
