pub fn is_valid(s: String) -> bool {
    let pairs: Vec<(char, char)> = vec![('}', '{'), (')', '('), (']', '[')];

    if s.len() % 2 != 0 {
        return false;
    }

    if !pairs.iter().any(|(_, opening)| s.chars().next().unwrap() == *opening) {
        return false;
    }

    let mut stack: Vec<char> = Vec::new();
    for c in s.chars() {
        if !pairs.iter().any(|(closing, _)| *closing == c) {
            stack.push(c);
        } else if let Some((closing, opening)) = pairs.iter().find(|&&(closing, _)| closing == c) {
            if let Some(&top) = stack.last() {
                if top == *opening {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
    }
    stack.is_empty()
}
