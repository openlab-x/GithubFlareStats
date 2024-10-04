# GithubFlareStats

![GitHub Stats](../logo/logo_v1.png)

## حول

**GithubFlareStats** هو أداة مفتوحة المصدر مصممة لإنشاء صور ديناميكية قابلة للتخصيص لعرض إحصائيات مستخدمي GitHub. يدعم العديد من السمات ويسمح لك بتضمين هذه الإحصائيات في ملف README الشخصي على GitHub أو أي منصة تدعم Markdown. اعرض النجوم، الالتزامات، طلبات السحب، القضايا والمزيد بتنسيق جذاب بصريًا. تتيح مرونة هذه الأداة لأي شخص عرض إحصاءاته بالطريقة التي يفضلها.


### يمكنك قراءة هذا `README.md` بلغات أخرى

| التوافر  | اللغات | الرابط | آخر تحديث |
| :---:  | :---: | :---: |  :---: |
| ☑ | الإنجليزية | [README.md](https://github.com/openlab-x/GithubFlareStats/blob/main/README.md) | 04 أكتوبر 2024 |
| ☐ | اليابانية | [README_Ja.md](https://github.com/openlab-x/GithubFlareStats/blob/main/README_Translations/README_Ja.md) | 04 أكتوبر 2024 |
| ☐ | الكورية | [README_Ko.md](https://github.com/openlab-x/GithubFlareStats/blob/main/README_Translations/README_Ko.md) | 04 أكتوبر 2024 |
| ☐ | الصينية | [README_Zh.md](https://github.com/openlab-x/GithubFlareStats/blob/main/README_Translations/README_Zh.md) | 04 أكتوبر 2024 |
| ☑ | الألمانية | [README_De.md](https://github.com/openlab-x/GithubFlareStats/blob/main/README_Translations/README_De.md) | 04 أكتوبر 2024 |
| ☐ | الإسبانية | [README_Es.md](https://github.com/openlab-x/GithubFlareStats/blob/main/README_Translations/README_Es.md) | 04 أكتوبر 2024 |
| ☐ | العربية | [README_Ar.md](https://github.com/openlab-x/GithubFlareStats/blob/main/README_Translations/README_Ae.md) | 04 أكتوبر 2024 |
| ☐ | العبرية | [README_He.md](https://github.com/openlab-x/GithubFlareStats/blob/main/README_Translations/README_He.md) | 04 أكتوبر 2024 |
| ☐ | الأوكرانية | [README_Uk.md](https://github.com/openlab-x/GithubFlareStats/blob/main/README_Translations/README_Uk.md) | 04 أكتوبر 2024 |
| ☐ | الروسية | [README_Ru.md](https://github.com/openlab-x/GithubFlareStats/blob/main/README_Translations/README_Ru.md) | 04 أكتوبر 2024 |



## جدول المحتويات

- [حول](#حول)
- [الميزات](#الميزات)
- [البدء](#البدء)
- [المنصات المختبرة](#المنصات-المختبرة)
- [العرض التوضيحي المباشر والأمثلة](#العرض-التوضيحي-المباشر-والأمثلة)
  - [التخصيص](#التخصيص)
  - [روابط الأمثلة](#روابط-الأمثلة)
- [الاستخدام](#الاستخدام)
- [تقنية التكديس](#تقنية-التكديس)
- [المساهمة](#المساهمة)
- [الشكر والتقدير](#الشكر-والتقدير)
- [الإبلاغ عن الأخطاء](#الإبلاغ-عن-الأخطاء)
- [الترخيص](#الترخيص)
- [الاتصال](#الاتصال)

## الميزات

- **عرض إحصائيات GitHub**: عرض إجمالي النجوم، الالتزامات، طلبات السحب، القضايا، المناقشات، المتابعين والمساهمات.
- **ثيمات قابلة للتخصيص**: تعديل ألوان الخلفية، النص، والبطاقات عبر معلمات URL لتتناسب مع أسلوب ملفك الشخصي.
- **صديق للتضمين**: يدعم تضمين Markdown لملفات README في GitHub والمنصات الأخرى التي تدعم Markdown.
- **متجاوب**: يتكيف ديناميكيًا مع الشاشات المختلفة وسياقات الاستخدام.


## البدء
- **التبعيات**: Python3, Flask, Pillow<br/><br/>
- أولاً، قم بتثبيت Flask و Pillow

```bash
pip install flask
pip install pillow
```
- ثم قم باستنساخ المستودع وتشغيل `run.py`
```cmd
git clone https://github.com/openlab-x/GithubFlareStats.git
cd GithubFlareStats
python run.py
```
من المهم جدًا التأكد من أن مكتباتك محدثة إلى أحدث إصدار، حيث أن هذه هي الإصدارات المستخدمة في هذا المستودع.

## المنصات المختبرة
- [x] الويب: يعمل بشكل كامل على المتصفحات الرئيسية مثل Chrome و Firefox و Edge.
- [x] GitHub Readme-md.
- [x] Readme-md محلي.
- [x] معاينة Readme في Visual Studio Code.
- [x] كصورة خارجية لأي موقع.
- [x] كـ Iframe.


## العرض التوضيحي المباشر والأمثلة:

  - **الوضع الفاتح - مباشر:**

  - https://github.com/ajee10x
  - ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/ajee10x?response=image&bgColor=%23ffffff&textColor=%23000000&cardColor=%23e1e1e1&chartColor=%23007bff&chartTextColor=black)
  - [Made With GithubFlareStats](https://github.com/openlab-x/GithubFlareStats)


  - **الوضع الداكن - مباشر:**

  - https://github.com/Alaa-abdulridha
  - ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/Alaa-abdulridha?response=image&bgColor=%231e1e1e&textColor=%23f0f0f0&cardColor=%23333&chartColor=%23ff9800&chartTextColor=white)
  - [Made With GithubFlareStats](https://github.com/openlab-x/GithubFlareStats)

### التخصيص

| المعامل | الوصف |
| --- | --- |
| bgColor | لون الخلفية (مثال: #ffffff) |
| textColor | لون النص (مثال: #000000) |
| cardColor | لون خلفية البطاقة (مثال: #e1e1e1) |
| chartColor | لون أشرطة الرسم البياني (مثال: #007bff) |
| chartTextColor | لون نص تسميات الرسم البياني (مثال: أسود) |



### روابط الأمثلة

  - **مثال على تضمين الوضع الفاتح:**

  ```md
    ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/ajee10x?response=image&bgColor=%23ffffff&textColor=%23000000&cardColor=%23e1e1e1&chartColor=%23007bff&chartTextColor=black)
- [Made With GithubFlareStats](https://github.com/openlab-x/GithubFlareStats)
  ```
  - **مثال على تضمين الوضع الداكن:**

  ```md
    ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/torvalds?response=image&bgColor=%231e1e1e&textColor=%23f0f0f0&cardColor=%23333&chartColor=%23ff9800&chartTextColor=white)
- [Made With GithubFlareStats](https://github.com/openlab-x/GithubFlareStats)
  ```


## الاستخدام

1. استبدل ajee10x/torvalds باسم مستخدم GitHub الخاص بك في رابط العرض التوضيحي:

  ```md
    ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/your-username?response=image))
- [Made With GithubFlareStats](https://github.com/openlab-x/GithubFlareStats)
  ```
2. الصق هذا الرابط في ملف README الخاص بك أو في أي محتوى يدعم Markdown لعرض إحصائيات GitHub الخاصة بك.

  ```md
    ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/your-username?response=image&bgColor=%23f0f0f0&textColor=%23000000&cardColor=%23d9e6f2&chartColor=%23007bff&chartTextColor=black))
- [Made With GithubFlareStats](https://github.com/openlab-x/GithubFlareStats)
  ```
3. باستخدام رابط مخصص، سيبدو الرابط الخاص بك كما يلي.

  ```md
    ![GitHub Stats](https://[YOUR-URL].com/githubflarestats/api/gitfs.php/your-username?response=image))
  ```

## تقنية التكديس
- الخلفية: Python (Flask لتوليد الصور)
- الواجهة الأمامية: HTML, CSS, JavaScript (لمعاينة السمات وصفحة العرض التوضيحي)
- معالجة الصور: Pillow (مكتبة الصور في Python)
- تخزين البيانات المؤقت: تم تنفيذه لتقليل طلبات API وتخزين الصور مؤقتًا لمدة 24 ساعة.
- الوكيل: تم استخدام PHP كوكيل خفيف لتوجيه الطلبات وإدارة التخزين المؤقت.
- الاستضافة: تم نشره في بيئة استضافة جاهزة للإنتاج.
- الأمان: تم اختبار البرنامج ضد الثغرات الشائعة، ولا سيما XSS وSQL Injection. يمكنك تشغيله بأمان على الخادم الخاص بك!


## المساهمة
نرحب بالمساهمات! إليك كيفية المساعدة:
  
  1. امنح المشروع نجمة.
  2. تابعنا على GitHub.
  3. تابعنا على وسائل التواصل الاجتماعي.
  4. اعمل Fork للمستودع.
  5. أنشئ فرعًا جديدًا لميزتك أو لإصلاح الأخطاء.
  6. قم بإجراء التغييرات الخاصة بك.
  7. قدم طلب سحب (Pull Request).
  8. يرجى التأكد من تحديث الاختبارات حسب الحاجة.



## الشكر والتقدير
- Python: لغة البرمجة المستخدمة في الخلفية لهذا المشروع.
- Pillow: لتمكين التلاعب بالصور وعرضها في Python.
- GitHub API: لتوفير البيانات المستخدمة في إنشاء إحصائيات المستخدم.
- يتم تحديث الإحصائيات تلقائيًا كل 24 ساعة لمنع الطلبات المفرطة على API وضمان كفاءة الخدمة وتجنب تجاوز حدود الطلب.
- جميع المساهمين: شكرًا لكل من ساهم في هذا المشروع.
- فريق OpenLabX: شكر خاص للفريق على تطوير المشروع وصيانته.


## الإبلاغ عن الأخطاء
- إذا وجدت خطأ في هذا المشروع، لا تتردد في التواصل مع فريقنا.
- إذا كنت تشعر بالمساعدة، يرجى التفكير في إصلاح الخطأ وتقديم طلب سحب (Pull Request).
- نقدم شكرنا الجزيل لأي شخص يبلغ عن أخطاء أو يقوم بإصلاحها في هذا المشروع.

  
## الترخيص
هذا المشروع مرخص بموجب [رخصة MIT](https://github.com/openlab-x/GithubFlareStats/blob/main/LICENSE).

## الاتصال

في السعي نحو الابتكار،  
**فريق OpenLabX**

- **الموقع الإلكتروني**: [https://openlabx.com](https://openlabx.com)
- **البريد الإلكتروني**: contact@openlabx.com

**تابعنا:**


- [Instagram](https://www.instagram.com/openlabx_official/)
- [X (formerly Twitter)](https://x.com/openlabx)
- [Facebook](https://www.facebook.com/openlabx/)
- [YouTube](https://www.youtube.com/@OpenLabX)
- [GitHub](https://github.com/openlab-x)
