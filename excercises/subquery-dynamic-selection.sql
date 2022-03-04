use db1;  
SELECT Guides_title, guides_revenue 
FROM guides
    WHERE guides_revenue = (
      select MAX(cast(guides_revenue AS UNSIGNED))
      from guides
    );

