def mapgen(p):
	# undirectional weighted graph for distance calculation
	path_map = {
				# left hand
				# pinky
				p[0,0]: { p[1,0]: 1.9636, p[2,0]: 3.8396 },
				p[1,0]: { p[0,0]: 1.9636, p[2,0]: 2.1298 },
				p[2,0]: { p[0,0]: 3.8396, p[1,0]: 2.1298 },

				# ring
				p[0,1]: { p[1,1]: 1.9636, p[2,1]: 3.8396 },
				p[1,1]: { p[0,1]: 1.9636, p[2,1]: 2.1298 },
				p[2,1]: { p[0,1]: 3.8396, p[1,1]: 2.1298 },

				# middle
				p[0,2]: { p[1,2]: 1.9636, p[2,2]: 3.8396 },
				p[1,2]: { p[0,2]: 1.9636, p[2,2]: 2.1298 },
				p[2,2]: { p[0,2]: 3.8396, p[1,2]: 2.1298 },

				# index
				p[0,3]: {
					p[1,3]: 1.9636, p[2,3]: 3.8396, p[0,4]: 1.9050,
					p[1,4]: 3.0495, p[2,4]: 4.0691, p[2,5]: 5.0626
				},
				p[1,3]: {
					p[0,3]: 1.9636, p[2,3]: 2.1298, p[0,4]: 2.3812,
					p[1,4]: 1.9050, p[2,4]: 2.1298, p[2,5]: 3.4343
				},
				p[2,3]: {
					p[0,3]: 3.8396, p[1,3]: 2.1298, p[0,4]: 4.4929,
					p[1,4]: 3.4343, p[2,4]: 1.9050, p[2,5]: 3.8100
				},
				p[0,4]: {
					p[0,3]: 1.9050, p[1,3]: 2.3812, p[2,3]: 4.4929,
					p[1,4]: 1.9636, p[2,4]: 3.8396, p[2,5]: 4.0691
				},
				p[1,4]: {
					p[0,3]: 3.0495, p[1,3]: 1.9050, p[2,3]: 3.4343,
					p[0,4]: 1.9636, p[2,4]: 2.1298, p[2,5]: 2.1298
				},
				p[2,4]: {
					p[0,3]: 4.0691, p[1,3]: 2.1298, p[2,3]: 1.9050,
					p[0,4]: 3.8396, p[1,4]: 2.1298, p[2,5]: 1.9050
				},

				# B key (hand agnostic)
				p[2,5]: {
					p[0,3]: 5.0626, p[1,3]: 3.4343, p[2,3]: 3.8100,
					p[0,4]: 4.0691, p[1,4]: 2.1298, p[2,4]: 1.9050,
					p[0,5]: 3.8396, p[1,5]: 2.1298, p[0,6]: 4.4929,
					p[1,6]: 3.4343, p[2,6]: 1.9050, p[2,7]: 3.8100
				},

				# right hand
				# index
				p[0,5]: {
					p[1,5]: 1.9636, p[0,6]: 1.9050, p[1,6]: 3.0495,
					p[2,6]: 4.0691, p[2,7]: 5.0626, p[2,5]: 3.8396
				},
				p[1,5]: {
					p[0,5]: 1.9636, p[0,6]: 2.3812, p[1,6]: 1.9050,
					p[2,6]: 2.1298, p[2,7]: 3.4343, p[2,5]: 2.1298
				},
				p[0,6]: {
					p[0,5]: 1.9050, p[1,5]: 2.3812, p[1,6]: 1.9636,
					p[2,6]: 3.8396, p[2,7]: 4.0691, p[2,5]: 4.4929
				},
				p[1,6]: {
					p[0,5]: 3.0495, p[1,5]: 1.9050, p[0,6]: 1.9636,
					p[2,6]: 2.1298, p[2,7]: 2.1298, p[2,5]: 3.4343
				},
				p[2,6]: {
					p[0,5]: 4.0691, p[1,5]: 2.1298, p[0,6]: 3.8396,
					p[1,6]: 2.1298, p[2,7]: 1.9050, p[2,5]: 1.9050
				},
				p[2,7]: {
					p[0,5]: 5.0626, p[1,5]: 3.4343, p[0,6]: 4.0691,
					p[1,6]: 2.1298, p[2,6]: 1.9050, p[2,5]: 3.8100
				},

				# middle
				p[0,7]: { p[1,7]: 1.9636, p[2,8]: 4.0691 },
				p[1,7]: { p[0,7]: 1.9636, p[2,8]: 2.1298 },
				p[2,8]: { p[0,7]: 4.0691, p[1,7]: 2.1298 },

				# ring
				p[0,8]: { p[1,8]: 1.9636, p[2,9]: 4.0691 },
				p[1,8]: { p[0,8]: 1.9636, p[2,9]: 2.1298 },
				p[2,9]: { p[0,8]: 4.0691, p[1,8]: 2.1298 },

				# pinky
				p[0,9]: {
					p[1,9]:  1.9636, p[0,10]: 1.9050, p[1,10]: 3.0495,
					p[2,10]: 4.0691, p[0,11]: 3.8100, p[1,11]: 4.6905
				},
				p[1,9]: {
					p[0,9]:  1.9636, p[0,10]: 2.3812, p[1,10]: 1.9050,
					p[2,10]: 2.1298, p[0,11]: 3.8396, p[1,11]: 3.8100
				},
				p[0,10]: {
					p[0,9]:  1.9050, p[1,9]:  2.3812, p[1,10]: 1.9636,
					p[2,10]: 3.8396, p[0,11]: 1.9050, p[1,11]: 3.0495
				},
				p[1,10]: {
					p[0,9]:  3.0495, p[1,9]:  1.9050, p[0,10]: 1.9636,
					p[2,10]: 2.1298, p[0,11]: 2.3812, p[1,11]: 1.9050
				},
				p[2,10]: {
					p[0,9]:  4.0691, p[1,9]:  2.1298, p[0,10]: 3.8396,
					p[1,10]: 2.1298, p[0,11]: 4.4929, p[1,11]: 3.4343
				},
				p[0,11]: {
					p[0,9]:  3.8100, p[1,9]:  3.8396, p[0,10]: 1.9050,
					p[1,10]: 2.3812, p[2,10]: 4.4929, p[1,11]: 1.9636
				},
				p[1,11]: {
					p[0,9]:  4.6905, p[1,9]:  3.8100, p[0,10]: 3.0495,
					p[1,10]: 1.9050, p[2,10]: 3.4343, p[0,11]: 1.9636
				}
	}

	return path_map
