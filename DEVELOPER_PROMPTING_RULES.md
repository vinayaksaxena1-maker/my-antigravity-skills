# Developer Prompting Rules for App Generation (Hinglish)

Normal users aur developer/app creators ke prompting tareeqe me bohot farq hota hai. Ek creator ke roop me AI se production-ready, clean aur low-token consuming code likhwane ke liye ye rules follow karein.

---

## 1. The 4 Pillars of Developer Prompting

### Pillar A: Tech Stack & Architecture Pehle Batayein
* **Bad:** *"Mujhe ek panchang screen bana do."*
* **Good:** *"Hum React + TypeScript + Tailwind CSS ka use kar rahe hain. PanchangScreen.tsx ko `src/components/` me ek alag modular file me banayein. State management local rahega."*

### Pillar B: Abstract Ke Bajay Technical Specs Dein
* **Bad:** *"Aisa function banao jo daily muhurats calculate kare."*
* **Good:** *"Ek TypeScript helper function `getDailyMuhurats(panchang: PanchangInfo): MuhuratItem[]` banayein, jisme shubh/ashubh muhurats ke logic process hote hon."*

### Pillar C: Incremental Growth (MVP First)
* **Bad:** *"Mera poora clock app ek baar me hi complete code likh do."*
* **Good:** *"Step 1: Pehle sirf outer aur inner rings ka static SVG elements group layout set karein. Koi runtime animations ya dynamic logic abhi mat daalein. Jab main check kar lu, tab aage badhenge."*

### Pillar D: Error Handling & Edge Cases
* **Bad:** *"Weather fetch karne ka code likho."*
* **Good:** *"API call ke liye fetch/axios use karein. Loading indicator, API offline failure, aur invalid city error ko handle karein. Error aane par page white screen hone ke bajay ek toast alert show karein."*

---

## 2. Standard Developer Prompt Template
Bhavishya me jab bhi koi naya module ya feature banana ho, toh is structure me prompt likhein:

```text
[CONTEXT]: Main ek [proejct name] par kaam kar raha hoon.
[STACK]: React (TS) + Tailwind + Lucide Icons.
[ARCHITECTURAL RULES]:
  - Components split hone chahiye (<300 lines).
  - Hardcoded colors ke bajay global CSS variables use karein.
[TASK]: Mujhe [Feature name] banana hai.
[DETAILS]:
  1. [Step 1 description]
  2. [Step 2 description]
[VERIFICATION]: Code likhne ke baad backup banayein aur compilation check karein.
```

---

## 3. Benefits of This Approach
* **Zero Rework:** AI directly aapke codebase ke design system ko follow karega.
* **Token Saving:** Precise commands se output tokens 85% tak bachegi.
* **Super-Fast Delivery:** Debugging cycles kam honge aur code compile-ready banega.
