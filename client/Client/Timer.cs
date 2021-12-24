using System;
using System.Windows.Threading;

namespace Client
{
    internal class Timer
    {
        private DispatcherTimer timer;
        public Timer(EventHandler handler, int ms = 500)
        {
            timer = new DispatcherTimer();
            timer.Interval = TimeSpan.FromMilliseconds(ms);
            timer.Tick += handler;
        }

        public void Start()
        {
            if (!timer.IsEnabled)
                timer.Start();
        }

        public void Stop()
        {
            if (timer.IsEnabled)
                timer.Stop();
        }
    }
}
