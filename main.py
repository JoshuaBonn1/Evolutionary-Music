from generation import Generation
import lilypond

def main():
    g = Generation(size=100, elite=0.05, mutate=0.10, tournament=10, mood=raw_input())
    g.run(100, desired_length=13)
    g.best.info()
    lilypond.printPiece(g.best, 'best.ly')
    lilypond.printPiece(g.worst, 'worst.ly')
    

if __name__ == '__main__':
    main()