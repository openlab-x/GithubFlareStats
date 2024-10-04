# GithubFlareStats

![GitHub Stats](../logo/logo_v1.png)

## Über

**GithubFlareStats** ist ein Open-Source-Tool, das entwickelt wurde, um dynamische, anpassbare Bilder zur Anzeige von GitHub-Benutzerstatistiken zu erstellen. Es unterstützt mehrere Themes und ermöglicht es, diese Statistiken in dein GitHub-Profil-README oder auf andere markdown-unterstützte Plattformen einzubetten. Zeige Sterne, Commits, Pull Requests, Issues und vieles mehr in einem optisch ansprechenden Format. Die Vielseitigkeit dieses Tools erlaubt es jedem, seine Statistiken auf die gewünschte Weise darzustellen.

## Inhaltsverzeichnis

- [Über](#über)
- [Funktionen](#funktionen)
- [Erste Schritte](#erste-schritte)
- [Getestete Plattformen](#getestete-plattformen)
- [Live-Demo und Beispiele](#live-demo-und-beispiele)
  - [Anpassung](#anpassung)
  - [Beispiel-URLs](#beispiel-urls)
- [Verwendung](#verwendung)
- [Technologie-Stack](#technologie-stack)
- [Beitragen](#beitragen)
- [Danksagungen](#danksagungen)
- [Fehlerbericht](#fehlerbericht)
- [Lizenz](#lizenz)
- [Kontakt](#kontakt)


## Funktionen

- **GitHub-Statistiken anzeigen**: Zeige Gesamtsterne, Commits, PRs, Issues, Diskussionen, Follower und Beiträge an.
- **Anpassbare Themes**: Ändere Hintergrund-, Text- und Kartenfarben über URL-Parameter, um das Profil individuell anzupassen.
- **Einbettungsfreundlich**: Unterstützt die Markdown-Einbettung für GitHub-Profil-Readme-Dateien und andere markdown-unterstützte Plattformen.
- **Responsive**: Passt sich dynamisch an verschiedene Bildschirme und Nutzungskontexte an.

## Erste Schritte
- **Abhängigkeiten**: Python3, Flask, Pillow<br/><br/>
- Zuerst Flask und Pillow installieren
```bash
pip install flask
pip install pillow
```
- Dann das Repository klonen und `run.py` ausführen
```cmd
git clone https://github.com/openlab-x/GithubFlareStats.git
cd GithubFlareStats
python run.py
```
Es ist sehr wichtig, sicherzustellen, dass deine Bibliotheken auf die neueste Version aktualisiert sind, da diese Versionen in diesem Repository verwendet werden.

## Getestete Plattformen
- [x] Web: Voll funktionsfähig in den gängigen Browsern wie Chrome, Firefox und Edge.
- [x] GitHub Readme-md.
- [x] Lokales Readme-md.
- [x] Visual Studio Code Readme-Vorschau.
- [x] Als externes Bild für jede Webseite.
- [x] Als Iframe.

## Live-Demo und Beispiele:

  - **Light Mode - Live:**
  - https://github.com/ajee10x
  - ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/ajee10x?response=image&bgColor=%23ffffff&textColor=%23000000&cardColor=%23e1e1e1&chartColor=%23007bff&chartTextColor=black)
  - [Made With GithubFlareStats](https://github.com/openlab-x/GithubFlareStats)


  - **Dark Mode - Live:**
  - https://github.com/Alaa-abdulridha
  - ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/Alaa-abdulridha?response=image&bgColor=%231e1e1e&textColor=%23f0f0f0&cardColor=%23333&chartColor=%23ff9800&chartTextColor=white)
  - [Made With GithubFlareStats](https://github.com/openlab-x/GithubFlareStats)

### Anpassung

| Parameter | Beschreibung |
| --- | --- |
| bgColor | Hintergrundfarbe (z.B. #ffffff) |
| textColor | Textfarbe (z.B. #000000) |
| cardColor | Hintergrundfarbe der Karte (z.B. #e1e1e1) |
| chartColor | Farbe der Diagrammbalken (z.B. #007bff) |
| chartTextColor | Textfarbe der Diagrammbeschriftungen (z.B. schwarz) |



### Beispiel-URLs

  - **Einbettungsbeispiel für Light Mode:**
  ```md
    ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/ajee10x?response=image&bgColor=%23ffffff&textColor=%23000000&cardColor=%23e1e1e1&chartColor=%23007bff&chartTextColor=black)
- [Made With GithubFlareStats](https://github.com/openlab-x/GithubFlareStats)
  ```
  - **Einbettungsbeispiel für Dark Mode:**
  ```md
    ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/torvalds?response=image&bgColor=%231e1e1e&textColor=%23f0f0f0&cardColor=%23333&chartColor=%23ff9800&chartTextColor=white)
- [Made With GithubFlareStats](https://github.com/openlab-x/GithubFlareStats)
  ```


## Verwendung

1. Ersetze ajee10x/torvalds durch deinen GitHub-Benutzernamen in der Demo-URL:
  ```md
    ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/your-username?response=image))
- [Made With GithubFlareStats](https://github.com/openlab-x/GithubFlareStats)
  ```
2. Füge diesen Link in dein README oder in anderen markdown-unterstützten Inhalt ein, um deine GitHub-Statistiken anzuzeigen.
  ```md
    ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/your-username?response=image&bgColor=%23f0f0f0&textColor=%23000000&cardColor=%23d9e6f2&chartColor=%23007bff&chartTextColor=black))
- [Made With GithubFlareStats](https://github.com/openlab-x/GithubFlareStats)
  ```
3. Mit einer benutzerdefinierten URL sieht dein Link so aus.
  ```md
    ![GitHub Stats](https://[YOUR-URL].com/githubflarestats/api/gitfs.php/your-username?response=image))
  ```

## Technologie-Stack
- Backend: Python (Flask für die Bereitstellung der Bildgenerierung)
- Frontend: HTML, CSS, JavaScript (für Theme-Vorschau und Demo-Seite)
- Bildbearbeitung: Pillow (Python Imaging Library)
- Daten-Caching: Implementiert, um API-Aufrufe zu reduzieren und Bilder für 24 Stunden zu cachen.
- Proxy: PHP wird als leichter Proxy verwendet, um Anfragen weiterzuleiten und Caching zu verwalten.
- Hosting: Bereitgestellt in einer produktionsbereiten Hosting-Umgebung.
- Sicherheit: Die Software wurde auf häufige Schwachstellen, insbesondere XSS und SQL-Injection, getestet. Du kannst diese Software sicher auf deinem Server ausführen!

## Beitragen
 Wir freuen uns über Beiträge! So kannst du helfen:
  
  1. Gib dem Projekt einen Stern.
  2. Folge uns auf GitHub.
  3. Folge uns in den sozialen Medien.
  4. Forke das Repository.
  5. Erstelle einen neuen Branch für dein Feature oder deinen Bugfix.
  6. Nimm deine Änderungen vor.
  7. Reiche einen Pull Request ein.
  8. Stelle bitte sicher, dass du die Tests entsprechend aktualisierst.


## Danksagungen
- Python: Die Programmiersprache, die für das Backend dieses Projekts verwendet wird.
- Pillow: Für die Ermöglichung der Bildmanipulation und -wiedergabe in Python.
- GitHub API: Für die Bereitstellung der Daten zur Generierung der Benutzerstatistiken.
- Statistiken werden alle 24 Stunden automatisch aktualisiert, um übermäßige API-Anfragen zu vermeiden und sicherzustellen, dass der Dienst effizient bleibt und keine Ratenlimits überschreitet.
- Alle Mitwirkenden: Vielen Dank an alle, die zu diesem Projekt beigetragen haben.
- OpenLabX Team: Ein besonderer Dank an das Team für die Entwicklung und Wartung des Projekts.

## Fehlerbericht
- Wenn du einen Fehler in diesem Projekt findest, zögere bitte nicht, unser Team zu kontaktieren.
- Wenn du hilfsbereit bist, ziehe in Betracht, den Fehler zu beheben und einen Pull Request zu erstellen.
- Wir danken allen herzlich, die Fehler melden oder beheben.
  
## Lizenz
Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).

## Kontakt

Im Streben nach Innovation,  
**OpenLabX Team**

- **Website**: [https://openlabx.com](https://openlabx.com)
- **E-Mail**: contact@openlabx.com

**Folge uns:**

- [Instagram](https://www.instagram.com/openlabx_official/)
- [X (formerly Twitter)](https://x.com/openlabx)
- [Facebook](https://www.facebook.com/openlabx/)
- [YouTube](https://www.youtube.com/@OpenLabX)
- [GitHub](https://github.com/openlab-x)
