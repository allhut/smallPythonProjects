import webbrowser
import time

break_t = 3;

print ("This program run at ", time.ctime());
while break_t != 0:
    time.sleep(180);
    webbrowser.open("https://www.youtube.com/watch?v=7F37r50VUTQ");
    break_t = break_t - 1;

print ("done");
