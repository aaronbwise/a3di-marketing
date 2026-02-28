# Case Study File Templates

Reference these exact patterns when scaffolding a new case study. Replace all `{{PLACEHOLDER}}` values with actual content. All file paths are relative to `../website/landing_page_react/`.

---

## File 1: `../website/landing_page_react/src/content/case-studies/{{slug}}.jsx`

```jsx
import CaseStudySection from '../../components/case-study/CaseStudySection'
// Only import these if needed:
// import MermaidDiagram from '../../components/case-study/MermaidDiagram'
// import CodeBlock from '../../components/case-study/CodeBlock'
import TakeawayBox from '../../components/case-study/TakeawayBox'

// Only include if user provided a Mermaid diagram:
// const diagramChart = `flowchart LR
//     A["Step 1"] --> B["Step 2"]
//     B --> C["Step 3"]`

// Only include if user provided a code snippet:
// const codeSnippet = `{
//   "key": "value"
// }`

export default function {{PascalName}}Content() {
  return (
    <>
      <CaseStudySection title="Challenge">
        <p className="text-[0.95rem] leading-[1.7]">
          {{challenge_paragraph_1}}
        </p>
        <p className="text-[0.95rem] leading-[1.7]">
          {{challenge_paragraph_2}}
        </p>
      </CaseStudySection>

      <CaseStudySection title="Approach">
        <p className="text-[0.95rem] leading-[1.7]">
          {{approach_paragraph_1}}
        </p>

        {/* Only include if user provided a diagram: */}
        {/* <MermaidDiagram chart={diagramChart} /> */}

        <p className="text-[0.95rem] leading-[1.7]">
          {{approach_paragraph_2}}
        </p>

        {/* Only include if user provided a code snippet: */}
        {/* <CodeBlock filename="{{code_filename}}" code={codeSnippet} /> */}
      </CaseStudySection>

      <CaseStudySection title="Result">
        <p className="text-[0.95rem] leading-[1.7]">
          {{result_paragraph_1}}
        </p>
        <p className="text-[0.95rem] leading-[1.7]">
          {{result_paragraph_2}}
        </p>
      </CaseStudySection>

      <TakeawayBox>
        <h2 className="font-bold text-[1.3rem] mb-3">Key Takeaway</h2>
        <p className="text-[0.95rem] leading-[1.7]">
          {{takeaway_text}}
        </p>
      </TakeawayBox>
    </>
  )
}
```

---

## File 2: `../website/landing_page_react/src/content/caseStudies.js` — append to array

Add this object inside the `caseStudies` array (before the closing `]`):

```js
  {
    slug: '{{slug}}',
    title: '{{title}}',
    subtitle: '{{subtitle}}',
    tags: [{{tags}}],
    // Only include these two lines if a client logo was provided:
    // clientLogo: '/img/{{logo_filename}}',
    // clientLogoAlt: '{{client_name}} logo',
    meta: {
      title: 'A3DI | {{title}}',
      description: '{{subtitle}}.',
      ogType: 'article',
      ogUrl: 'https://www.a3di.dev/case-studies/{{slug}}',
      ogImage: 'https://www.a3di.dev/img/optimized_logo.png',
    },
    metaBar: [
      { label: 'Client', value: '{{client_name}}' },
      { label: 'Sector', value: '{{sector}}' },
      { label: 'Countries', value: '{{countries}}' },
      // Add any additional metaBar items the user provided here
      { label: 'Duration', value: '{{duration}}' },
    ],
  },
```

---

## File 3: `../website/landing_page_react/src/pages/CaseStudyDetailPage.jsx` — two edits

### Edit A: Add import (after existing content imports)

```js
import {{PascalName}}Content from '../content/case-studies/{{slug}}'
```

### Edit B: Add to contentMap object

```js
const contentMap = {
  'alive-and-thrive': AliveAndThriveContent,
  '{{slug}}': {{PascalName}}Content,    // ← add this line
}
```

---

## Slug-to-PascalCase conversion

Convert the kebab-case slug to a PascalCase component name by:
1. Split on hyphens
2. Capitalize the first letter of each segment
3. Join and append `Content`

Examples:
- `wfp-dashboard` → `WfpDashboardContent`
- `alive-and-thrive` → `AliveAndThriveContent`
- `unicef-wash-survey` → `UnicefWashSurveyContent`
