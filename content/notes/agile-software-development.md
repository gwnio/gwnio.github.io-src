Title: Agile Software Development
Date: 2017-02-07 11:10:23 -0400
Summary: These are just some basic notes that I took while doing some research on agile softwarement development.
Tags: tech, agile, software development

## Table of contents
1. [Defined](#defined)
2. [Philosophy](#paragraph1)
    1. [Adaptive vs Predictive](#adaptive_vs_predictive)
    2. [Code vs Document](#code_vs_document)
3. [Overview](#overview)
4. [Values](#values)
5. [Principles](#principles)
6. [Agile Methods](#agile_methods)
    1. [Agile Practices](#agile_practices)
7. [Measuring Agility](#measuring_agility)
8. [Experience](#experience)
    1. [Large-scale](#large-scale)
    2. [Agile Pitfalls](#agile_pitfalls)

### Defined <a name="defined"></a>

Group of software development methods in which requirements and solutions evolve through collaboration between self-organizing, cross-functional teams.  Promotes adaptive planning, evolutionary development, early delivery, continuous improvement, encourages rapid and flexible response to change.  Conceptual framework to deliver working software with minimum amount of work.

### Philosophy <a name="philosophy"></a>

Agile development is targeted at complex systems and projects with dynamic, non deterministic, and non-linear characteristics.  Stable plans and predictions are often hard to get at early stages.  Big up-front designs cause waste and are not economically sound.

#### Adaptive vs Predictive <a name="adaptive_vs_predictive"></a>

Agile is on the adaptive side of the continuum.  An adaptive team will have difficulty describing what will happen in the future and they also cannot report what exactly they will do next week.

Use risk analysis to choose between adaptive (agile) and predictive (plan-driven) methods.  [See chart in the section](https://en.wikipedia.org/wiki/Agile_software_development#Adaptive_vs._predictive){:target="_blank"}.

#### Code vs Document <a name="code_vs_document"></a>
Documentation should be just barely good enough (JBGE).  Too much documentation is usually  a waste and out of sync with the code.  Too little documentation may cause problems for maintenance, communication, learning, and knowledge sharing.  When documenting ask your, "what would you want to know if you joined the team tomorrow".

### Overview <a name="overview"></a>
* Iterations
  * plan, req. gather, design, code, unit test, acceptance test
  * multiple iterations required to release product or new feature(s)
* Efficiency and face-to-face communication
  * customer-rep or stakeholder available to developers for mid-iteration questions
  * information radiator - large board displaying status of software product
* Short feedback
  * brief meeting with team members to discuss where they are, days work, and roadblocks
* Quality focus
  * tools and techniques to improve quality and enhance project agility
  * continuous integration, unit testing, test-driven development, design patterns, code refactoring

### Values <a name="values"></a>
* Pair programming
* Working software more important than just presenting documents to clients in meetings
* Requirements cannot be fully collected at the beginning of development process, so continuous customer and stakeholder involvement is very important
* Quick responses to change and continuous development

### Principles <a name="principles"></a>
* Welcome changing requirements
* Working software delivered frequently
* Close, daily cooperation between business people and developers
* Continuous attention to good design
* Self-organizing teams
* Regular adaptation to changing circumstances

### Agile Methods <a name="agile_methods"></a>

#### Agile Practices <a name="agile_practices"></a>
[See](http://en.wikipedia.org/wiki/Agile_software_development#Agile_practices){:target="_blank"}

### Measuring Agility <a name="measuring_agility"></a>
Agility measurement index - scores against 5 dimensions of development (duration, risk, novelty, effort, and interaction).  Nokia test, Karlskrona test

### Experience <a name="experience"></a>

#### Large-scale <a name="large-scale"></a>
* Things that may negatively impact a agile project:
* Large-scale development (>20 developers)
* Forcing agile process on development team
* Mission critical (i.e. software for avionics)

#### Agile Pitfalls <a name="agile_pitfalls"></a>

##### Product owner role not properly filled
Product owner role filled by a development team member.  The business has to be accountable or the agile ecosystem breaks down.  The development team needs prioritization and feedback from the business.

##### Problem solving in daily scrum
If problem solving occurs it often does so so with certain team members and is not best use of entire team's time.  Table problem solving for sub-team meeting following daily scrum.

##### Assigning tasks
A tendency is for assignors to box team members into certain roles (team member A always does database work).  Prevents stretching team member's abilities and prevents cross-training opportunities.

##### Lack of automated testing
Having automated testing framework to take care of system and integration tests is a safety net against regressions from new development and introduction of new defects to code refactoring.