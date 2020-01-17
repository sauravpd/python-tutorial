def main():
    try:
        x=int('Test')
        print(x)
    except ValueError:
        print("ValueError")
if __name__=='__main__' : main()