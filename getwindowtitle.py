import pygetwindow as gw

# Get all open window titles
titles = gw.getAllTitles()

# Print non-empty titles
window_title="Baldur's Gate - Enhanced Edition - v2.6.6.0"
    # Get the window
windows = gw.getWindowsWithTitle(window_title)
if windows:
    win = windows[0]
    print(f"Window: '{win.title}' height - '{win.height}' width - '{win.width}' top -'{win.top}' left -'{win.left}' right -'{win.right}' bottom -'{win.bottom}")

    
else:
    print("Window not found.")
