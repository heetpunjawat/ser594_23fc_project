#### SER594: Experimentation
#### (title) MotoViz: Mapping Motorcycle Crash Data 
#### (author) Heet Punjawat
#### (date) 11/20/2023

## Explainable Records
### Record 1
**Raw Data:** 
- First Harmful Event Type: Collision with Motor Vehicle in Transport
- Lighting Conditions: Daylight
- Road Surface Condition: Dry
- Operator Age Involvement: 25-29 years
- Helmet Use: Yes
- Type of Violation: No violation
**Prediction Explanation:** The model correctly predicted a low severity (PDO Crashes) for a daytime collision with a motor vehicle in transport, dry road conditions, an operator aged 25-29 using a helmet with no violation. In the domain of motorcycle safety, the conditions described, including daylight, dry road surface, helmet use, and no violation, are typically associated with a lower risk of severe crashes. Daylight conditions provide good visibility, dry roads reduce the likelihood of skidding or loss of control, helmet use enhances rider safety, and no violation implies adherence to traffic rules, all contributing to a lower predicted severity.

### Record 2
**Raw Data:**
- First Harmful Event Type: Overturning
- Lighting Conditions: Dark - Lighted
- Road Surface Condition: Wet
- Operator Age Involvement: 40-44 years
- Helmet Use: No
- Type of Violation: Speeding
**Prediction Explanation:** The model accurately predicted a higher severity (Injury Crashes) for a nighttime overturning incident with wet road conditions, an operator aged 40-44 not using a helmet, and involving speeding. In the domain of motorcycle safety, nighttime conditions, wet road surfaces, absence of helmet use, and speeding are factors associated with increased crash severity. Reduced visibility during nighttime, coupled with wet roads, makes control more challenging. The absence of a helmet increases the risk of injury, and speeding further elevates the severity of potential crashes. Therefore, the model's prediction aligns with the expected outcomes based on these risk factors.

## Interesting Features
### Feature A
**Feature:** First Harmful Event Type
**Justification:** The choice of "First Harmful Event Type" as Feature A is crucial due to the diverse nature of motorcycle crashes. Different types of events can lead to varying degrees of harm and severity. For example, a collision with a motor vehicle in transport might result in different outcomes compared to an overturning incident or a collision with a fixed object. The specific event type sets the initial conditions of the crash and influences subsequent interactions, making it a pivotal factor in determining the severity. Therefore, variations in the "First Harmful Event Type" are expected to significantly impact the prediction as certain events inherently pose higher risks of severe outcomes in motorcycle crashes.

### Feature B
**Feature:** Helmet Use
**Justification:** Helmet use is a critical factor in motorcycle safety and is expected to have a substantial impact on crash severity. Helmets provide a protective barrier for the rider's head and reduce the risk of severe head injuries in the event of a crash. The presence or absence of a helmet can influence the extent of harm and the severity of injuries sustained by the rider. Domain knowledge strongly supports the idea that proper helmet use is associated with a lower likelihood of severe outcomes, while the absence of a helmet increases the risk of injury. Therefore, variations in "Helmet Use" are anticipated to significantly influence the model's prediction, reflecting the well-established relationship between helmet use and motorcycle crash severity.

## Experiments 
### Varying A
**Prediction Trend Seen:** Varying the First Harmful Event Type produced distinct predictions, unveiling valuable insights into the model's interaction with this feature. For instance, collisions with pedestrians or bicyclists tended to yield higher predicted severities compared to collisions with non-fixed objects. This suggests that the nature of the first harmful event plays a crucial role in determining the severity of the crash. The trend aligns with domain knowledge, as events involving vulnerable road users, such as pedestrians or bicyclists, often result in more severe consequences.

### Varying B
**Prediction Trend Seen:** Experimenting with Helmet Use as Feature B demonstrated its significant impact on predictions. When helmets were used, the predicted severity tended to be lower. This trend underscores the importance of helmet safety in mitigating the severity of motorcycle crashes. The model appears to recognize the protective effect of helmets, leading to lower predicted severities when riders use this safety equipment.

### Varying A and B together
**Prediction Trend Seen:** Combining variations in First Harmful Event Type (A) and Helmet Use (B) provided further insights. Collisions with pedestrians or bicyclists, coupled with no helmet use, consistently resulted in higher predicted severities compared to other scenarios. This suggests an additive effect, where the combination of a potentially severe event and the absence of helmet protection leads to higher predicted crash severities.

### Varying A and B inversely
**Prediction Trend Seen:** Varying A and B inversely, even with potentially severe events, such as collisions with pedestrians, helmet use consistently led to lower predicted severities. This highlights the protective influence of helmets, which can mitigate the severity of crashes irrespective of the specific event type.

In summary, the experiments reveal that the model responds sensibly to variations in First Harmful Event Type and Helmet Use, aligning with domain expectations and providing valuable insights into the causal mechanisms influencing crash severity predictions.
