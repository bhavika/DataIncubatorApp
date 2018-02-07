import copy
import pytest


def stable_matching(m_prefs, w_prefs):
    men = sorted(m_prefs.keys())
    women = sorted(w_prefs.keys())

    # Initialize all m ∈ m_prefs and w ∈ w_prefs to free
    men_free = men[:]

    paired = {}
    m_copy = copy.deepcopy(m_prefs)
    w_copy = copy.deepcopy(w_prefs)

    while men_free:
        man = men_free.pop(0)
        man_prefs = m_copy[man]
        woman = man_prefs.pop(0)
        partner = paired.get(woman)
        if not partner:
            # This woman was not paired with any man, so we pair her now.
            paired[woman] = man
        else:
            woman_prefs = w_copy[woman]

            # Check whether the woman prefers someone else over her current partner and update the pairing accordingly.
            if woman_prefs.index(partner) > woman_prefs.index(man):
                paired[woman] = man

                # The previous partner is now free and back into the available pool.
                if m_copy[partner]:
                    men_free.append(partner)
            else:
                if woman_prefs:
                    woman_prefs.append(man)
    return paired


def isStable(pairs, m_prefs, w_prefs):
    for woman, man in pairs.items():
        i = m_prefs[man].index(woman)

        # find the man's preferences besides the woman he got paired with
        other_preferences = m_prefs[man][:i]

        for op in other_preferences:
            partner = pairs[woman]

            # Check if the woman prefers another man over the one paired with her
            # If this is true even for one pair - the matches we generated are unstable and we exit early.
            if w_prefs[op].index(man) < w_prefs[op].index(partner):
                return False
    return True


if __name__ == '__main__':
    m_prefs = {'A1': ['B3', 'B2', 'B4', 'B1'], 'A2': ['B4', 'B3', 'B1', 'B2'], 'A3': ['B2', 'B1', 'B3', 'B4'],
               'A4': ['B1', 'B2', 'B3', 'B4']}
    w_prefs = {'B1': ['A2', 'A1', 'A3', 'A4'], 'B2': ['A1', 'A4', 'A2', 'A3'], 'B3': ['A3', 'A2', 'A4', 'A1'],
               'B4': ['A3', 'A1', 'A2', 'A4']}
    pairs = stable_matching(m_prefs, w_prefs)

    for k, v in sorted(pairs.items()):
        print(k, v)

    print(isStable(pairs, m_prefs, w_prefs))
