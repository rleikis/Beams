import numpy as N
import gtk.gdk

class DeltaDetector(object):

    def __init__(self, active=False, threshold=20.0):
        self._previous_frame = None
        self._frame = None
        self.active = active
        self.threshold = threshold
    
    def send_frame(self, frame):
        self._previous_frame = self._frame
        self._frame = N.array(frame, dtype=float)
        
        if not self.active:
            return
        if self._previous_frame is None:
            return
        if(self._previous_frame.shape != self._frame.shape):
            self._previous_frame = None
            return
        
        if N.max(N.abs(self._frame - self._previous_frame)) > self.threshold:
            gtk.gdk.beep()

    # Properties
    @property
    def active(self):
        return self._active
    
    @active.setter
    def active(self, value):
        self._active = bool(value)
    
    @property
    def threshold(self):
        return self._threshold
    
    @threshold.setter
    def threshold(self, value):
        self._threshold = float(value)
    
    @property
    def average(self):
        if self._frame is None or self._previous_frame is None:
            return 0.0
        return N.mean(self._frame - self._previous_frame)
    