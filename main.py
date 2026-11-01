import sys
import io
from datetime import datetime

# Đảm bảo in tiếng Việt chuẩn trên mọi console
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Xin chào! Môi trường của tôi đã sẵn sàng cho khóa học AI Agent 101!")
print(f"Thời gian hiện tại: {current_time}")
