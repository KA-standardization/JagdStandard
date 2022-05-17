python -m cProfile -s cumulative julia1_nopil.py
python -m cProfile -o profile.stats julia1_nopil.py

>>> import pstats
>>> p=pstats.Stats("profile.stats")
>>> p.sort_stats("cumulative")
<pstats.Stats object at 0x000001718DBB8780>
>>> p.print_stats()
>>> p.print_callers()
>>> p.print_callees()

