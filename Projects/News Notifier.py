import time
import notify2
from sample_news import topStories


Icon_path="F:\Projects\Join the GIFLORD Discord Server!.jpeg"

newsitems=topStories()

notify2.init("News Notifier")

n=notify2.Notification(None,icon=Icon_path)

n.set_urgency(notify2.URGENCY_NORMAL)

n.set_timeout(10000)

for newsitem in newsitems:
    n.update(newsitem['title'],newsitem['description'])

    n.show()

    time.sleep(15)