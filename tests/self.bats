load harness

@test "self-1" {
  check '2 - 3' '-1'
}

@test "self-2" {
  check '1 - 2 + 5' '4'
}

@test "self-3" {
  check '25 - 5 * 3' '10'
}

@test "self-4" {
  check '6 + 2 * 3 - 2' '10'
}

@test "self-5" {
  check '9 * 1000 + 19 * 21 - 9' '9390'
}