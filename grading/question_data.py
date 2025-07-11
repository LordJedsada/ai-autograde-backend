# grading/question_data.py

questions = {
    1: {
    
      "1_1": "เปรียบเทียบความแตกต่างระหว่าง AI, ML และ DL",
      "1_2": "จงอธิบายประเภทของ Machine Learning และยกตัวอย่างของแต่ละประเภท",
      "1_3": "Deep Learning ทำงานอย่างไร? และเพราะเหตุใดจึงเป็นที่นิยมในงานที่เกี่ยวข้องกับภาพและเสียง",
      "1_4": "อธิบายบทบาทของข้อมูล (Data) ในกระบวนการเรียนรู้ของ AI/ML/DL และผลที่เกิดขึ้นเมื่อข้อมูลมีคุณภาพต่ำ",
      "1_5": "จงอธิบายว่าโครงข่ายประสาทเทียม (Artificial Neural Network) เลียนแบบการทำงานของสมองมนุษย์อย่างไร",
      "1_6": "ยกตัวอย่างงานที่ AI สามารถทำได้ดีกว่ามนุษย์ และงานที่ยังไม่สามารถทดแทนมนุษย์ได้",
      "1_7": "AI มีผลกระทบทางบวกและลบต่อสังคมอย่างไร? ยกตัวอย่างประกอบ",
      "1_8": "หากคุณต้องการเริ่มเรียนรู้ AI/ML/DL คุณจะเริ่มต้นอย่างไร? ระบุลำดับขั้นพื้นฐาน",
      "1_9": "คุณคิดว่าในอนาคต AI จะสามารถแทนที่มนุษย์ได้ทั้งหมดหรือไม่? จงแสดงความคิดเห็นโดยพิจารณาทั้งด้านเทคโนโลยี จริยธรรม และสังคม",
      "1_10": "ให้นักเรียนยกตัวอย่างการใช้งาน AI ในชีวิตประจำวัน และอธิบายว่า AI นั้นช่วยปรับปรุงหรือแก้ปัญหาอะไรให้กับผู้ใช้บ้าง",
    },

    2: {
      "2_1": "อธิบายหลักการทำงานของคำสั่ง input() ใน Python",
      "2_2": "อธิบายความหมายและการใช้งาน if statement ใน Python",
      "2_3": "ฟังก์ชันใน Python คืออะไรและทำงานอย่างไร?",
      "2_4": "อธิบายความหมายของ while loop ใน Python และให้ตัวอย่างการใช้งาน",
      "2_5": "การจัดการข้อผิดพลาดใน Python ทำได้อย่างไร?",
      "2_6": "อธิบายการใช้ for loop ใน Python",
      "2_7": "การใช้งาน list ใน Python คืออะไรและใช้ทำอะไร?",
      "2_8": "อธิบายความแตกต่างระหว่าง append() และ extend() ใน Python",
      "2_9": "อธิบายการใช้ try-except เพื่อจัดการข้อผิดพลาด",
      "2_10": "อธิบายความหมายของ lambda function ใน Python",
    },
    
    3: {
      "3_1": "ไลบรารี PIL ย่อมาจากอะไร และใช้สำหรับทำอะไรใน Python?",
      "3_2": "ฟังก์ชันใดใน PIL ที่ใช้แปลงภาพสีให้เป็นภาพขาวดำ?",
      "3_3": "คำสั่งใดใน OpenCV ที่ใช้แปลงภาพจาก BGR ไปเป็น Grayscale?",
      "3_4": "หากต้องการโหลดภาพใน OpenCV ให้ใช้คำสั่งอะไร?",
      "3_5": "หากต้องการแสดงภาพด้วย OpenCV บนหน้าต่างใหม่ ต้องใช้คำสั่งอะไร?",
      "3_6": "หลังจากแสดงภาพด้วย cv2.imshow() แล้ว เราควรใช้คำสั่งใดเพื่อรอการกดปุ่มจากผู้ใช้ก่อนปิดหน้าต่าง?",
      "3_7": "คำสั่งใดใน OpenCV ที่ใช้วาดกรอบสี่เหลี่ยมรอบใบหน้าหรือวัตถุ?",
      "3_8": "ไลบรารี OpenCV ใช้โมเดลอะไรในการตรวจจับใบหน้าแบบง่าย?",
      "3_9": "หากต้องการบันทึกภาพที่ถูกแก้ไขใหม่ใน OpenCV ใช้คำสั่งใด?",
      "3_10": "หากต้องการปิดหน้าต่างทั้งหมดที่แสดงภาพใน OpenCV ควรใช้คำสั่งใด?",
    },

    4: {
      "4_1": "อธิบายการใช้งานโมดูล sounddevice ใน Python",
      "4_2": "อธิบายการใช้งาน scipy.io.wavfile ในการบันทึกและอ่านไฟล์เสียง",
      "4_3": "วิธีการแปลงเสียงเป็นข้อความโดยใช้ Speech Recognition ใน Python คืออะไร?",
      "4_4": "การแปลงข้อความเป็นเสียง (Text-to-Speech) ทำได้อย่างไร?",
      "4_5": "ฟังก์ชัน sounddevice.play() ใช้ทำอะไร?",
      "4_6": "การใช้ pydub library ในการตัดต่อเสียงทำงานอย่างไร?",
      "4_7": "อธิบายการใช้ SpeechRecognition ในการรับเสียงจากไมโครโฟน",
      "4_8": "วิธีการบันทึกเสียงจากไมโครโฟนด้วย sounddevice คืออะไร?",
      "4_9": "อธิบายการใช้ scipy.io.wavfile ในการจัดการไฟล์เสียง WAV",
      "4_10": "ฟังก์ชัน pydub.AudioSegment.from_file() ใช้ทำอะไร?",
    },

    5: {
      "5_1": "อธิบายโครงสร้างของ Perceptron และหลักการทำงาน",
      "5_2": "อธิบายการใช้งาน Activation Functions ในโครงข่ายประสาทเทียม",
      "5_3": "อธิบายการใช้งาน Convolutional Neural Network (CNN) ในการจำแนกรูปภาพ",
      "5_4": "อธิบายการทำงานของ Backpropagation ในการฝึกโครงข่ายประสาทเทียม",
      "5_5": "อธิบายกระบวนการฝึกโมเดล Deep Neural Network (DNN)",
      "5_6": "อธิบายการใช้ Dropout ในการป้องกันการ Overfitting ในการฝึกโมเดล",
      "5_7": "อธิบายความแตกต่างระหว่าง Activation Function แบบ Sigmoid และ ReLU",
      "5_8": "อธิบายบทบาทของ Optimizer ในการฝึก Deep Learning Models",
      "5_9": "อธิบายข้อดีและข้อเสียของการใช้ Batch Normalization ในโครงข่ายประสาทเทียม",
      "5_10": "อธิบายวิธีการทำงานของ Long Short-Term Memory (LSTM) และการใช้งานในงานที่เกี่ยวข้องกับลำดับ",
    },

    6: {
      "6_1": "อธิบายโมดูล dobotapi ในการควบคุมหุ่นยนต์ Dobot Magician บน Python",
      "6_2": "วิธีการเชื่อมต่อหุ่นยนต์ Dobot Magician กับ Python ต้องตั้งค่าอะไรบ้าง?",
      "6_3": "อธิบายฟังก์ชัน ConnectDobot() ที่ใช้เชื่อมต่อหุ่นยนต์ Dobot Magician",
      "6_4": "หากต้องการตรวจสอบว่าเชื่อมต่อหุ่นยนต์กับ Python สำเร็จหรือไม่ ควรทำอย่างไร?",
      "6_5": "อธิบายขั้นตอนในการติดตั้งไลบรารีและไดรเวอร์ที่จำเป็นก่อนใช้งาน Dobot Magician ใน Python",
      "6_6": "ฟังก์ชัน MoveTo() ใช้ในการเคลื่อนที่ของหุ่นยนต์ Dobot Magician อย่างไร?",
      "6_7": "อธิบายการใช้งานคำสั่ง MoveL() เพื่อให้หุ่นยนต์ Dobot เคลื่อนที่ในลักษณะ Linear",
      "6_8": "การเคลื่อนที่ของหุ่นยนต์ Dobot Magician ใช้หน่วยวัดอะไรในการกำหนดตำแหน่ง?",
      "6_9": "อธิบายการใช้คำสั่ง emergencyStop() ในกรณีที่หุ่นยนต์ Dobot ต้องการหยุดทันที",
      "6_10": "ฟังก์ชัน getPosition() ใช้เพื่อดึงข้อมูลตำแหน่งปัจจุบันของหุ่นยนต์ Dobot อย่างไร?",
    },

    7: {
      "7_1": "อธิบายการใช้พิกัด X, Y, Z ในการควบคุมตำแหน่งของหุ่นยนต์ Dobot",
      "7_2": "ฟังก์ชัน MoveTo() ใช้ในการเคลื่อนที่ของหุ่นยนต์ Dobot อย่างไร?",
      "7_3": "อธิบายการทำงานของฟังก์ชัน MoveL() ในการเคลื่อนที่ของหุ่นยนต์ Dobot",
      "7_4": "อธิบายการใช้งานฟังก์ชัน getPosition() เพื่อดึงข้อมูลตำแหน่งปัจจุบันของหุ่นยนต์",
      "7_5": "อธิบายวิธีการหยุดหุ่นยนต์ทันทีในกรณีฉุกเฉิน",
      "7_6": "อธิบายการใช้งานฟังก์ชัน setPosition() ในการตั้งค่าตำแหน่งของหุ่นยนต์",
      "7_7": "การควบคุมการเคลื่อนที่ของหุ่นยนต์ในรูปแบบเชื่อมโยงตำแหน่งมีวิธีการอย่างไร?",
      "7_8": "อธิบายวิธีการตั้งค่าความเร็วในการเคลื่อนที่ของหุ่นยนต์ Dobot",
      "7_9": "อธิบายการใช้คำสั่ง getPose() ในการตรวจสอบสถานะของหุ่นยนต์",
      "7_10": "การควบคุมหุ่นยนต์ Dobot เพื่อให้ทำงานในพื้นที่จำกัดต้องคำนึงถึงปัจจัยอะไรบ้าง?",
    },

    8: {
      "8_1": "อธิบายหลักการของการใช้ Feature Matching ในการคัดแยกวัตถุในภาพ",
      "8_2": "การใช้ Dobot ในการคัดแยกวัตถุมีข้อดีอย่างไร?",
      "8_3": "อธิบายการทำงานของ Convolutional Neural Networks (CNN) ในการจำแนกวัตถุในภาพ",
      "8_4": "การตั้งตำแหน่งฐานกล้องร่วมกับการใช้งาน Dobot ควรคำนึงถึงอะไร?",
      "8_5": "อธิบายกระบวนการการตรวจจับวัตถุในภาพด้วยเทคนิค Object Detection",
      "8_6": "ทำไมการใช้ Mask R-CNN ถึงเหมาะสมกับการคัดแยกวัตถุที่มีความซับซ้อนในภาพ?",
      "8_7": "การใช้ภาพที่มีความละเอียดสูงในการคัดแยกวัตถุมีข้อดีอะไร?",
      "8_8": "ทำไมการเลือกฟีเจอร์ที่เหมาะสมจึงสำคัญในกระบวนการ Feature Matching?",
      "8_9": "อธิบายการใช้ CNN ในการจำแนกประเภทของวัตถุจากภาพที่มีหลายคลาส",
      "8_10": "การใช้ Dobot ร่วมกับกล้องในการคัดแยกวัตถุช่วยเพิ่มประสิทธิภาพในการทำงานอย่างไร?",
    },

    9: {
      "9_1": "อธิบายหลักการทำงานของ Natural Language Processing (NLP) ในการสั่งงานหุ่นยนต์ผ่านข้อความ",
      "9_2": "คุณสมบัติหลักของโมเดลภาษา LLM (Large Language Model) คืออะไร และทำไมมันถึงเหมาะกับการสนทนา",
      "9_3": "การใช้งานไมโครโฟนในการสั่งงานหุ่นยนต์ด้วยเสียงต้องการการประมวลผลใดบ้าง",
      "9_4": "อธิบายการใช้คำสั่ง Transformer ในการประมวลผลข้อความสำหรับการสั่งงานหุ่นยนต์",
      "9_5": "การสร้าง Prompt ที่เหมาะสมในการสั่งงานหุ่นยนต์ควรคำนึงถึงอะไรบ้าง",
      "9_6": "อธิบายวิธีการที่โมเดล LLM ช่วยให้หุ่นยนต์สามารถเข้าใจคำสั่งจากผู้ใช้งานได้อย่างถูกต้อง",
      "9_7": "อธิบายวิธีการที่หุ่นยนต์สามารถเข้าใจคำสั่งจากผู้ใช้ผ่านข้อความที่ไม่เป็นทางการหรือสแลง",
      "9_8": "อธิบายการทำงานของฟังก์ชัน Natural Language Understanding (NLU) ในการสั่งงานหุ่นยนต์ด้วยข้อความ",
      "9_9": "การใช้ระบบสั่งงานด้วยเสียงกับหุ่นยนต์มีข้อดีและข้อเสียอย่างไร?",
      "9_10": "อธิบายวิธีการที่หุ่นยนต์สามารถสั่งงานผ่านข้อความในสถานการณ์ที่มีคำสั่งที่ซับซ้อน",
    },

    10: {
      "10_1": "การใช้ Cloud ในการเก็บข้อมูลการทำงานของหุ่นยนต์ช่วยในเรื่องใดบ้าง?",
      "10_2": "อธิบายกระบวนการของการทำ Logging ในระบบหุ่นยนต์",
      "10_3": "การใช้ระบบ Cloud Logging ช่วยให้สามารถติดตามประสิทธิภาพของหุ่นยนต์ได้อย่างไร?",
      "10_4": "ทำไมการเลือกใช้รูปแบบ CSV ในการบันทึกข้อมูลจึงเป็นทางเลือกที่ดีสำหรับการทำ Logging?",
      "10_5": "อธิบายการใช้ฟังก์ชัน fetchLog() ในการดึงข้อมูลจากระบบ Cloud",
      "10_6": "ความสำคัญของการตั้งค่าความปลอดภัยในการทำ Logging ข้อมูลใน Cloud คืออะไร?",
      "10_7": "อธิบายข้อดีของการใช้ Cloud Logging ในการจัดเก็บข้อมูลที่เกิดจากการทำงานของหุ่นยนต์",
      "10_8": "ทำไมการติดตามประวัติการทำงานของหุ่นยนต์ถึงสำคัญ?",
      "10_9": "อธิบายการใช้ฟังก์ชัน setAlert() ในระบบ Cloud Logging",
      "10_10": "การใช้ AWS ในการจัดการ Cloud Logging มีข้อดีอย่างไร?"
    }
}
